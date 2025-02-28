import redis.asyncio as redis

from taskcollabapi.core.env import env

redis_blocklist = redis.Redis(host=env.redis_host, port=env.redis_port, db=0)
