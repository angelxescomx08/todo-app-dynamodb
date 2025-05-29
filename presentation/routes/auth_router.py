from fastapi import APIRouter
from domain.dtos.user.create_user_dto import CreateUserDto
from database.database import table

auth_router = APIRouter()


@auth_router.post("/register")
def create_user(user: CreateUserDto):
    table.put_item(
        Item={
            "PK": "user",
            "SK": user.email,
            "email": user.email,
            "password": user.password,
        }
    )
    response = table.get_item(Key={"PK": "user", "SK": user.email})
    return response.get("Item")
