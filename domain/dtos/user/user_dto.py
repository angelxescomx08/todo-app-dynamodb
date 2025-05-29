from typing import Tuple


class UserDto:
    id: str
    email: str

    def __init__(self, id: str, email: str):
        self.id = id
        self.email = email

    @staticmethod
    def create(dict: dict) -> Tuple[str | None, "UserDto"]:
        id = dict["id"]
        email = dict["email"]
        if not id:
            return ["Id is required", None]
        if not email:
            return ["Email is required", None]

        return [None, UserDto(id, email)]
