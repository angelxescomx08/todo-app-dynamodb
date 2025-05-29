from pydantic import BaseModel


class User(BaseModel):
    id: str
    email: str
    password: str


class UserEntity:

    id: str
    email: str
    password: str

    def __init__(self, id: str, email: str, password: str):
        self.id = id
        self.email = email
        self.password = password

    @staticmethod
    def from_dict(data: dict) -> "UserEntity":
        id = data["id"]
        email = data["email"]
        password = data["password"]
        return UserEntity(id, email, password)
