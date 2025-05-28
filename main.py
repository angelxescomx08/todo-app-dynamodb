from fastapi import FastAPI
from mangum import Mangum
from presentation.routes.auth_router import auth_router
from presentation.routes.users_router import users_router

app = FastAPI()

app.include_router(auth_router, prefix="/auth")
app.include_router(users_router, prefix="/users")

handler = Mangum(app)
