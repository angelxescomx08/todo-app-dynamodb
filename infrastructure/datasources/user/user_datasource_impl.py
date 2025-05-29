from domain.datasources.user.user_datasource import UserDatasource
from domain.dtos.pagination.paginated_response import PaginatedResponse
from domain.dtos.user.create_user_dto import CreateUserDto
from domain.dtos.user.update_user_dto import UpdateUserDto
from domain.dtos.user.user_dto import UserDto
from database.database import table
from uuid import uuid4
from passlib.hash import bcrypt


class UserDatasourceImpl(UserDatasource):
    def create(user: CreateUserDto) -> UserDto:
        user_id = str(uuid4())
        hashed_password = bcrypt.hash(user.password)
        table.put_item(
            Item={
                "PK": f"user#{user_id}",
                "SK": user.email,
                "email": user.email,
                "password": hashed_password,
            }
        )
        response = table.get_item(Key={"PK": "user", "SK": user.email})
        user = response.get("Item")
        return UserDto.create(user)

    def get_users(self, page: int, limit: int) -> PaginatedResponse[UserDto]:
        pass

    def get_user_by_id(self, user_id: str) -> UserDto:
        pass

    def update(self, user: UpdateUserDto) -> UserDto:
        pass

    def delete(self, user_id: str) -> UserDto:
        pass
