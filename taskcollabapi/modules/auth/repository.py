from taskcollabapi.core.db.redis import redis_blocklist
from taskcollabapi.core.env import env


async def add_token_to_blocklist(jti: str, access_token: bool) -> None:
    expiration = env.jti_access_token_expire_in_seconds

    if not access_token:
        expiration = env.jti_refresh_token_expire_in_seconds

    await redis_blocklist.set(name=jti, value='token', ex=expiration)


async def token_in_blocklist(jti: str) -> bool:
    _jti = await redis_blocklist.get(jti)
    print(jti)
    print(redis_blocklist)

    return _jti is not None
