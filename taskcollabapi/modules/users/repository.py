from taskcollabapi.core.db.db import User, connect, db, disconnect
from taskcollabapi.modules.users.schema import UserCreateSchema


async def get_user_by_email(email: str) -> User | None:
    await connect()

    try:
        user = await db.user.find_unique(where={'email': email})
    finally:
        await disconnect()

    return user


async def create(data: UserCreateSchema) -> User:
    await connect()

    try:
        user = await db.user.create(data=data.model_dump())  # type: ignore
    finally:
        await disconnect()

    return user
