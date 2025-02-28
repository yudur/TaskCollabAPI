from taskcollabapi.errors.base import BaseError


class UserAlreadyExistsError(BaseError):
    def __init__(self):
        super().__init__(status=409, message='existing user', code='USER_ALREADY_EXISTS')


class InvalidCredentialsError(BaseError):
    def __init__(self):
        super().__init__(
            status=401,
            message='Incorrect email or password',
            code='INVALID_LOGIN_CREDENTIALS',
        )


class InvalidTokenError(BaseError):
    def __init__(self, message):
        super().__init__(
            status=401,
            message=message,
            code='INVALID_TOKEN',
        )


class AuthenticationNotFoundHeaderError(BaseError):
    def __init__(self):
        super().__init__(
            status=401,
            message='Authorization header is missing',
            code='MISSING_VALUE',
        )
