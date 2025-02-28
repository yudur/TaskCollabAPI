import uuid
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

import jwt
from passlib.context import CryptContext
from pydantic import BaseModel

from taskcollabapi.core.env import env


class TokenPayloadSchema(BaseModel):
    sub: str
    exp: int
    jti: str


# Security dependencies
pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


# generic function that creates twitter tokens with custom expiration time
def create_token(data: dict, expire_in: timedelta):
    to_encode = data.copy()

    expire = datetime.now(tz=ZoneInfo('UTC')) + expire_in
    to_encode.update({'exp': expire})

    # Generate a unique UUID for 'jti' (token identifier)
    jti = str(uuid.uuid4())
    to_encode.update({'jti': jti})

    encoded_jwt = jwt.encode(to_encode, env.secret_key, algorithm=env.jwt_algorithm)
    return encoded_jwt


# Create Access Token (JWT)
def create_access_token(email: str) -> str:
    token = create_token(
        {'sub': email}, timedelta(minutes=env.access_token_expire_minutes)
    )
    return token


# Create Refresh Token (JWT)
def create_refresh_token(email: str) -> str:
    token = create_token({'sub': email}, timedelta(days=env.refresh_token_expire_days))
    return token


# Decode JWT Token
def decode_token(token: str) -> TokenPayloadSchema | None:
    try:
        payload = jwt.decode(token, env.secret_key, algorithms=env.jwt_algorithm)

        return TokenPayloadSchema(
            sub=payload['sub'], exp=payload['exp'], jti=payload['jti']
        )

    except Exception:
        return None


# takes a password as an argument and returns an encrypted version of that password.
def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


# checks whether the password, when encrypted, matches the encrypted password.
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)
