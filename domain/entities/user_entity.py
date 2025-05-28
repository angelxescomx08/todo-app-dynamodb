from pydantic import BaseModel
from __future__ import annotations


class User(BaseModel):
    email: str
    password: str


class UserEntity:

    email: str
    password: str

    def __init__(self, email: str, password: str):
        self.email = email
        self.password = password

    @staticmethod
    def from_dict(data: dict) -> UserEntity:
        email = data["email"]
        password = data["password"]
        return UserEntity(email, password)
