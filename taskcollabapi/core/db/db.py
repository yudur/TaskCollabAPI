from typing import Callable, Coroutine, TypeAlias, TypeVar

import decorator

from prisma import Prisma
from prisma.models import *  # type: ignore # noqa: F403

T = TypeVar('T')
AsyncFuncType: TypeAlias = Callable[..., Coroutine[None, None, T]]

db = Prisma()


async def connect():
    await db.connect()


async def disconnect():
    await db.disconnect()


def with_db_connection(func: AsyncFuncType[T]) -> AsyncFuncType[T]:
    """
    Decorator to automatically manage the database connection.

    This decorator ensures that the database connection is opened before the function is
    executed and closed immediately after, avoiding connections that are not closed
    correctly.
    """

    @decorator.decorator
    async def wrapper(func: AsyncFuncType[T], *args, **kwargs) -> T:
        await connect()

        try:
            result = await func(*args, **kwargs)
        finally:
            await disconnect()

        return result

    return wrapper(func)
