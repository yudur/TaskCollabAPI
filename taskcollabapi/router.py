from fastapi import FastAPI

from .modules.users import users_controller


def create_router(app: FastAPI):
    app.include_router(users_controller.router, prefix='/users')
