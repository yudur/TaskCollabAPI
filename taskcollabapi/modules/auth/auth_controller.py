from fastapi import APIRouter, Depends, Response

from taskcollabapi.modules.auth import service
from taskcollabapi.modules.auth.dependencies import verify_refresh_token, verify_token
from taskcollabapi.modules.auth.schema import (
    CreateTokenResposeSchema,
    RegisterUserResponseSchema,
    SignInSchema,
    TokenDataType,
)
from taskcollabapi.modules.users.schema import UserCreateSchema

router = APIRouter(tags=['auth'])


@router.post('/signUp', status_code=201)
async def sign_up(data: UserCreateSchema) -> RegisterUserResponseSchema:
    return await service.sign_up(data)


@router.post('/signIn', status_code=200)
async def sign_in(data: SignInSchema, response: Response) -> CreateTokenResposeSchema:
    return await service.sign_in(data, response)


@router.post('/signOut', status_code=204)
async def sign_out(
    response: Response,
    access_token_data: TokenDataType = Depends(verify_token),
    refress_token_data: TokenDataType = Depends(verify_refresh_token),
) -> None:
    return await service.sign_out(response, access_token_data, refress_token_data)


@router.post('/refresh', status_code=200)
async def refresh_token(
    refress_token_data: TokenDataType = Depends(verify_refresh_token),
) -> CreateTokenResposeSchema:
    return await service.refresh_token(refress_token_data)
