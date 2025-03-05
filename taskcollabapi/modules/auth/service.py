from fastapi import Response

from taskcollabapi.core import security
from taskcollabapi.modules.auth import repository as auth_repo
from taskcollabapi.modules.auth.errors import (
    InvalidCredentialsError,
    UserAlreadyExistsError,
)
from taskcollabapi.modules.auth.schema import (
    CreateTokenResposeDict,
    RegisterUserResponseDict,
    SignInSchema,
    TokenData,
    TokenDataType,
)
from taskcollabapi.modules.users import repository as user_repo
from taskcollabapi.modules.users.schema import UserCreateSchema


async def sign_up(data: UserCreateSchema) -> RegisterUserResponseDict:
    user_exists = await user_repo.get_user_by_email(data.email)
    if user_exists:
        raise UserAlreadyExistsError()

    data.password = security.get_password_hash(data.password)

    user = await user_repo.create(data)

    return {
        'status': 201,
        'code': 'USER_CREATED',
        'message': 'User created successfully',
        'data': user,
    }


async def sign_in(data: SignInSchema, response: Response) -> CreateTokenResposeDict:
    user = await user_repo.get_user_by_email(data.email)
    if not user:
        raise InvalidCredentialsError()

    if not security.verify_password(data.password, user.password):
        raise InvalidCredentialsError()

    access_token = security.create_access_token(user.email)
    refresh_token = security.create_refresh_token(user.email)

    # sets a cookie containing the refresh token
    response.set_cookie(
        key='refresh_token', value=refresh_token, httponly=True, secure=True
    )

    return {
        'status': 200,
        'code': 'TOKEN_CREATED',
        'message': 'user authenticated and logged in successfully',
        'data': TokenData(access_token=access_token, token_type='Bearer'),
    }


async def sign_out(
    response: Response, access_token: TokenDataType, refresh_token: TokenDataType
) -> None:
    payload_access = access_token[1]
    payload_refresh = refresh_token[1]

    await auth_repo.add_token_to_blocklist(payload_access.jti, True)
    await auth_repo.add_token_to_blocklist(payload_refresh.jti, False)

    response.delete_cookie('refresh_token')


async def refresh_token(refresh_token: TokenDataType) -> CreateTokenResposeDict:
    payload = refresh_token[1]

    # Create a new access token
    new_access_token = security.create_access_token(payload.sub)

    return {
        'status': 200,
        'code': 'TOKEN_CREATED',
        'message': 'the token has been recreated',
        'data': TokenData(access_token=new_access_token, token_type='Bearer'),
    }
