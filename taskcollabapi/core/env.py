import dotenv
from pydantic_settings import BaseSettings

config = dotenv.load_dotenv()


class EnvSchema(BaseSettings):
    secret_key: str
    jwt_algorithm: str

    redis_host: str
    redis_port: int
    jti_access_token_expire_in_seconds: int
    jti_refresh_token_expire_in_seconds: int

    access_token_expire_minutes: float
    refresh_token_expire_days: float


env = EnvSchema()  # type: ignore
