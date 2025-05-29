from abc import ABC, abstractmethod
from domain.entities.user_entity import UserEntity
from domain.dtos.user.create_user_dto import CreateUserDto
from domain.dtos.user.user_dto import UserDto
from domain.repositories.user.user_repository import UserRepository


class RegisterUserUseCase(ABC):
    @abstractmethod
    def execute(self, email: str, password: str) -> UserDto:
        pass


class RegisterUser(RegisterUserUseCase):

    repository: UserRepository = None

    def __init__(self, repository: UserRepository):
        super().__init__()
        self.repository = repository

    def execute(self, user_dto: CreateUserDto) -> UserDto:
        return self.repository.create(user_dto)
