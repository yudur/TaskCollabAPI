from taskcollabapi.core.db.db import User, db, with_db_connection
from taskcollabapi.modules.users.schema import UserCreateSchema


@with_db_connection
async def get_user_by_email(email: str) -> User | None:
    user = await db.user.find_unique(where={'email': email})
    return user


@with_db_connection
async def create(data: UserCreateSchema) -> User:
    user = await db.user.create(data=data.model_dump())  # type: ignore
    return user
