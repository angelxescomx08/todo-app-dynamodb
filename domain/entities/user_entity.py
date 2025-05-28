from pydantic import BaseModel


class User(BaseModel):
    id: str
    email: str


class UserEntity:

    id: str
    email: str

    def __init__(self, id: str, email: str):
        self.id = id
        self.email = email

    @staticmethod
    def from_dict(data: dict) -> "UserEntity":
        id = data["id"]
        email = data["email"]
        return UserEntity(id, email)
