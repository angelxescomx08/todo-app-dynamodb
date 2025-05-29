from abc import ABC, abstractmethod
from domain.entities.user_entity import User
from domain.entities.paginated_response import PaginatedResponse
from domain.dtos.user.create_user_dto import CreateUserDto


class UserRepository(ABC):
    @abstractmethod
    def create(user: CreateUserDto) -> User:
        pass

    @abstractmethod
    def get_users(self, page: int, limit: int) -> PaginatedResponse[User]:
        pass

    @abstractmethod
    def get_user_by_id(self, user_id: str) -> User:
        pass

    @abstractmethod
    def update(self, user: User) -> User:
        pass

    @abstractmethod
    def delete(self, user_id: str) -> User:
        pass
