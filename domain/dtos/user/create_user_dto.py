from typing import Tuple
from pydantic import BaseModel


class CreateUserDto(BaseModel):
    email: str
    password: str

    @staticmethod
    def create(data: dict) -> Tuple[str | None, "CreateUserDto"]:
        email = data["email"]
        password = data["password"]
        if not email:
            return ["Email is required", None]
        if not password:
            return ["Password is required", None]
        return [None, CreateUserDto(email, password)]
