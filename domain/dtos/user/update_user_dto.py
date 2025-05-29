from typing import Tuple


class UpdateUserDto:
    id: str
    email: str | None
    password: str | None

    def __init__(self, id: str, email: str | None, password: str | None):
        self.id = id
        self.email = email
        self.password = password

    @staticmethod
    def create(dict: dict) -> Tuple[str | None, "UpdateUserDto"]:
        id = dict["id"]
        email = dict["email"]
        password = dict["password"]
        if not id:
            return ["Id is required", None]
        return [None, UpdateUserDto(id, email, password)]
