import boto3

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
    except client.exceptions.ResourceNotFoundException:
        # Si no existe, la creamos
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


# Aseguramos la existencia de la tabla antes de continuar
ensure_table_exists()

# Obtenemos la referencia a la tabla
table = dynamodb.Table(TABLE_NAME)
