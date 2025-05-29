from typing import Tuple
from pydantic import BaseModel


class UserDto(BaseModel):
    id: str
    email: str

    @staticmethod
    def create(data: dict) -> Tuple[str | None, "UserDto"]:
        id = data["id"]
        email = data["email"]
        if not id:
            return ["Id is required", None]
        if not email:
            return ["Email is required", None]

        return [None, UserDto(id, email)]
