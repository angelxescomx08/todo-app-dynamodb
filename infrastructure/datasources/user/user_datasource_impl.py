from domain.datasources.user.user_datasource import UserDatasource
from domain.dtos.pagination.paginated_response import PaginatedResponse
from domain.dtos.user.create_user_dto import CreateUserDto
from domain.dtos.user.update_user_dto import UpdateUserDto
from domain.dtos.user.user_dto import UserDto
from database.database import table
from uuid import uuid4
from passlib.hash import bcrypt
from fastapi.responses import Response


class UserDatasourceImpl(UserDatasource):
    def create(self, user: CreateUserDto) -> UserDto:
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
        response = table.get_item(Key={"PK": f"user#{user_id}", "SK": user.email})
        user = response.get("Item")
        if not user:
            return {
                "id": user_id,
            }
        user = {
            "id": user_id,
            "email": user["email"],
        }
        error, user = UserDto.create(user)
        if error:
            return Response(
                status_code=400,
                content={
                    "error": error,
                },
            )
        return user

    def get_users(self, page: int, limit: int) -> PaginatedResponse[UserDto]:
        pass

    def get_user_by_id(self, user_id: str) -> UserDto:
        pass

    def update(self, user: UpdateUserDto) -> UserDto:
        pass

    def delete(self, user_id: str) -> UserDto:
        pass
