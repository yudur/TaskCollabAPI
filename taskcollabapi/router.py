from fastapi import FastAPI

from taskcollabapi.modules.auth import auth_controller

from .modules.users import users_controller


def create_router(app: FastAPI):
    app.include_router(users_controller.router, prefix='/users')
    app.include_router(auth_controller.router, prefix='/auth')
