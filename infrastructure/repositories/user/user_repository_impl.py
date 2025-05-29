from domain.repositories.user.user_repository import UserRepository
from domain.dtos.pagination.paginated_response import PaginatedResponse
from domain.dtos.user.create_user_dto import CreateUserDto
from domain.dtos.user.update_user_dto import UpdateUserDto
from domain.dtos.user.user_dto import UserDto
from domain.datasources.user.user_datasource import UserDatasource


class UserRepositoryImpl(UserRepository):
    datasource: UserDatasource = None

    def __init__(self, datasource: UserDatasource):
        self.datasource = datasource

    def create(self, user: CreateUserDto) -> UserDto:
        return self.datasource.create(user)

    def get_users(self, page: int, limit: int) -> PaginatedResponse[UserDto]:
        return self.datasource.get_users(page, limit)

    def get_user_by_id(self, user_id: str) -> UserDto:
        return self.datasource.get_user_by_id(user_id)

    def update(self, user: UpdateUserDto) -> UserDto:
        return self.datasource.update(user)

    def delete(self, user_id: str) -> UserDto:
        return self.datasource.delete(user_id)
