from fastapi import APIRouter
from domain.entities.user_entity import User
from database.database import table

auth_router = APIRouter()


@auth_router.post("/register")
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
