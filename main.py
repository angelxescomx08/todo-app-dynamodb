from fastapi import FastAPI, Query
from mangum import Mangum
import boto3
from boto3.dynamodb.conditions import Key
from botocore.exceptions import ClientError
from pydantic import BaseModel

# Configuración de DynamoDB (local o AWS según corresponda)
dynamodb = boto3.resource(
    "dynamodb", region_name="us-west-2", endpoint_url="http://localhost:8000"
)
client = dynamodb.meta.client

# Nombre de la tabla que usaremos
TABLE_NAME = "AppDataTodoApp"


# Función para asegurar que la tabla exista
def ensure_table_exists():
    try:
        # Comprueba si la tabla ya existe
        client.describe_table(TableName=TABLE_NAME)
        print(f"La tabla '{TABLE_NAME}' ya existe.")
    except client.exceptions.ResourceNotFoundException:
        # Si no existe, la creamos
        print(f"La tabla '{TABLE_NAME}' no existe. Creando...")
        table = dynamodb.create_table(
            TableName=TABLE_NAME,
            KeySchema=[
                {"AttributeName": "PK", "KeyType": "HASH"},  # Clave de partición
                {"AttributeName": "SK", "KeyType": "RANGE"},  # Clave de ordenación
            ],
            AttributeDefinitions=[
                {"AttributeName": "PK", "AttributeType": "S"},  # Tipo String
                {"AttributeName": "SK", "AttributeType": "S"},  # Tipo String
            ],
            BillingMode="PAY_PER_REQUEST",  # Pago por demanda
        )
        # Esperar hasta que la tabla esté lista
        table.wait_until_exists()
        print(f"Tabla '{TABLE_NAME}' creada exitosamente.")


# Aseguramos la existencia de la tabla antes de continuar
ensure_table_exists()

# Obtenemos la referencia a la tabla
table = dynamodb.Table(TABLE_NAME)

# Inicializamos FastAPI
app = FastAPI()


# Modelo de usuario
class User(BaseModel):
    email: str
    password: str


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/auth/register")
def create_user(user: User):
    # Insertar usuario en DynamoDB
    table.put_item(
        Item={
            "PK": "user",
            "SK": user.email,
            "email": user.email,
            "password": user.password,
        }
    )
    # Devolver el ítem recién creado
    response = table.get_item(Key={"PK": "user", "SK": user.email})
    return response.get("Item")


def list_users(last_evaluated_key=None):
    params = {
        "KeyConditionExpression": Key("PK").eq("user"),
        "Limit": 10,
    }
    if last_evaluated_key:
        params["ExclusiveStartKey"] = last_evaluated_key

    response = table.query(**params)
    return response.get("Items", []), response.get("LastEvaluatedKey")


@app.get("/users")
def get_users(last_key: str | None = Query(None)):
    import json

    exclusive_start_key = json.loads(last_key) if last_key else None

    users, new_last_key = list_users(exclusive_start_key)
    return {
        "users": users,
        "last_key": new_last_key,
    }


handler = Mangum(app)
