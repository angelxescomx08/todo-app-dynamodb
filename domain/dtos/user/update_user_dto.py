from typing import Tuple
from pydantic import BaseModel


class UpdateUserDto(BaseModel):
    id: str
    email: str | None
    password: str | None

    @staticmethod
    def create(dict: dict) -> Tuple[str | None, "UpdateUserDto"]:
        id = dict["id"]
        email = dict["email"]
        password = dict["password"]
        if not id:
            return ["Id is required", None]
        return [None, UpdateUserDto(id, email, password)]
