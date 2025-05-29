from fastapi import APIRouter
from domain.dtos.user.create_user_dto import CreateUserDto
from infrastructure.datasources.user.user_datasource_impl import UserDatasourceImpl
from infrastructure.repositories.user.user_repository_impl import UserRepositoryImpl

auth_router = APIRouter()

datasource = UserDatasourceImpl()
repository = UserRepositoryImpl(datasource)


@auth_router.post("/register")
def create_user(user: CreateUserDto):
    return repository.create(user)
