from typing import Tuple

from pydantic import BaseModel, EmailStr

from taskcollabapi.core import security
from taskcollabapi.core.db.db import User
from taskcollabapi.schemas.responses import BaseResponseSchema

TokenDataType = Tuple[str, security.TokenPayloadSchema]


class RegisterUserResponseSchema(BaseResponseSchema):
    data: User


class SignInSchema(BaseModel):
    email: EmailStr
    password: str


class TokenData(BaseModel):
    access_token: str
    token_type: str


class CreateTokenResposeSchema(BaseResponseSchema):
    data: TokenData
