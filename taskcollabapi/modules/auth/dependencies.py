from fastapi import Request

from taskcollabapi.core import security
from taskcollabapi.modules.auth import repository as auth_repo
from taskcollabapi.modules.auth.errors import (
    AuthenticationNotFoundHeaderError,
    InvalidTokenError,
)
from taskcollabapi.modules.auth.schema import TokenDataType


async def verify_token(request: Request) -> TokenDataType:
    authorization = request.headers.get('Authorization')

    if not authorization:
        raise AuthenticationNotFoundHeaderError()

    # Checks if the token is of type "Bearer"
    if not authorization.startswith('Bearer '):
        raise InvalidTokenError('Token format is invalid. Please pass a Bearer token')

    token = authorization[7:]
    payload = security.decode_token(token)

    if not payload:
        raise InvalidTokenError('Invalid token')

    if await auth_repo.token_in_blocklist(payload.jti):
        raise InvalidTokenError('Token is revoked')

    return (token, payload)


async def verify_refresh_token(request: Request) -> TokenDataType:
    refresh_token = request.cookies.get('refresh_token')
    # Validate the refresh token
    if not refresh_token:
        raise InvalidTokenError('Missing refresh token')

    payload = security.decode_token(refresh_token)
    if not payload:
        raise InvalidTokenError('Invalid or expired refresh token')

    if await auth_repo.token_in_blocklist(payload.jti):
        raise InvalidTokenError('token revoked')

    return (refresh_token, payload)
