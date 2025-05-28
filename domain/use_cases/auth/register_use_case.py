from abc import ABC, abstractmethod
from domain.entities.user_entity import UserEntity
from domain.repositories.user.user_repository import UserRepository


class RegisterUserUseCase(ABC):
    @abstractmethod
    def execute(self, email: str, password: str) -> UserEntity:
        pass


class RegisterUser(RegisterUserUseCase):

    repository: UserRepository = None

    def __init__(self, repository: UserRepository):
        super().__init__()
        self.repository = repository

    def execute(self, email: str, password: str) -> UserEntity:
        user = UserEntity(email=email, password=password)
        return self.repository.create(user)
