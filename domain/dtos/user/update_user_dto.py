from typing import Tuple
from pydantic import BaseModel


class UpdateUserDto(BaseModel):
    id: str
    email: str | None
    password: str | None

    @staticmethod
    def create(data: dict) -> Tuple[str | None, "UpdateUserDto"]:
        id = data["id"]
        email = data["email"]
        password = data["password"]
        if not id:
            return ["Id is required", None]
        return [None, UpdateUserDto(id, email, password)]
