from prisma import Prisma
from prisma.models import *  # type: ignore # noqa: F403

db = Prisma()


async def connect():
    await db.connect()


async def disconnect():
    await db.disconnect()
