from abc import ABC, abstractmethod
from domain.entities.user_entity import UserEntity
from domain.entities.paginated_response import PaginatedResponse
from domain.dtos.user.create_user_dto import CreateUserDto
from domain.dtos.user.update_user_dto import UpdateUserDto


class UserDatasource(ABC):
    @abstractmethod
    def create(user: CreateUserDto) -> UserEntity:
        pass

    @abstractmethod
    def get_users(self, page: int, limit: int) -> PaginatedResponse[UserEntity]:
        pass

    @abstractmethod
    def get_user_by_id(self, user_id: str) -> UserEntity:
        pass

    @abstractmethod
    def update(self, user: UpdateUserDto) -> UserEntity:
        pass

    @abstractmethod
    def delete(self, user_id: str) -> UserEntity:
        pass
