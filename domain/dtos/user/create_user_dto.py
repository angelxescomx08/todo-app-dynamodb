from typing import Tuple


class CreateUserDto:
    email: str
    password: str

    def __init__(self, email: str, password: str):
        self.email = email
        self.password = password

    @staticmethod
    def create(dict: dict) -> Tuple[str | None, "CreateUserDto"]:
        email = dict["email"]
        password = dict["password"]
        if not email:
            return ["Email is required", None]
        if not password:
            return ["Password is required", None]
        return [None, CreateUserDto(email, password)]
