from abc import ABC, abstractmethod
from domain.dtos.pagination.paginated_response import PaginatedResponse
from domain.dtos.user.create_user_dto import CreateUserDto
from domain.dtos.user.update_user_dto import UpdateUserDto
from domain.dtos.user.user_dto import UserDto


class UserDatasource(ABC):
    @abstractmethod
    def create(self, user: CreateUserDto) -> UserDto:
        pass

    @abstractmethod
    def get_users(self, page: int, limit: int) -> PaginatedResponse[UserDto]:
        pass

    @abstractmethod
    def get_user_by_id(self, user_id: str) -> UserDto:
        pass

    @abstractmethod
    def update(self, user: UpdateUserDto) -> UserDto:
        pass

    @abstractmethod
    def delete(self, user_id: str) -> UserDto:
        pass
