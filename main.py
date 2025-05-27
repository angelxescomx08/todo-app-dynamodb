from fastapi import FastAPI, Query
from mangum import Mangum
import boto3
from boto3.dynamodb.conditions import Key
from pydantic import BaseModel

dynamodb = boto3.resource(
    "dynamodb", region_name="us-west-2", endpoint_url="http://localhost:8000"
)

# Intenta borrar la tabla si ya existe
try:
    table = dynamodb.Table("AppDataTodoApp")
    table.delete()
    table.wait_until_not_exists()
except dynamodb.meta.client.exceptions.ResourceNotFoundException:
    pass  # La tabla no existía, está bien continuar

table = dynamodb.create_table(
    TableName="AppDataTodoApp",
    KeySchema=[
        {"AttributeName": "PK", "KeyType": "HASH"},  # Partición clave
        {"AttributeName": "SK", "KeyType": "RANGE"},  # Sort key
    ],
    AttributeDefinitions=[
        {"AttributeName": "PK", "AttributeType": "S"},  # Partición clave
        {"AttributeName": "SK", "AttributeType": "S"},  # Sort key
    ],
    BillingMode="PAY_PER_REQUEST",  # El pago de escrituras y lecturas se realiza en base a la demanda
)

app = FastAPI()


class User(BaseModel):
    email: str
    password: str


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/auth/register")
def create_user(user: User):
    table.put_item(
        Item={
            "PK": "user",
            "SK": user.email,
            "email": user.email,
            "password": user.password,
        }
    )

    response = table.get_item(Key={"PK": "user", "SK": user.email})

    item = response.get("Item")

    return item


def list_users(table, last_evaluated_key=None):
    params = {
        "KeyConditionExpression": Key("PK").eq("user"),
        "Limit": 10,
    }
    if last_evaluated_key:
        params["ExclusiveStartKey"] = last_evaluated_key

    response = table.query(**params)
    users = response.get("Items", [])
    last_key = response.get("LastEvaluatedKey", None)  # para la próxima página
    return users, last_key


@app.get("/users")
def get_users(last_key: str | None = Query(None)):
    # last_key viene como JSON string, debes convertirlo a dict si existe
    import json

    exclusive_start_key = json.loads(last_key) if last_key else None

    users, new_last_key = list_users(table, exclusive_start_key)

    return {
        "users": users,
        "last_key": new_last_key,  # Pasa esto para la próxima página
    }


handler = Mangum(app)
