from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError

from taskcollabapi.errors.base import BaseError


def setup_error_handlers(app: FastAPI):
    """Sets up a global error handler"""

    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(req: Request, exc: RequestValidationError):
        # Catch Pydantic validation errors

        errors = []
        for error in exc.errors():
            field = '.'.join(str(loc) for loc in error['loc'])  # example: "body.email"
            errors.append({'field': field, 'message': error['msg']})

        return BaseError(
            status=422,
            message='Validation error in submitted fields.',
            code='VALIDATION_ERROR',
            data=errors,
        ).to_response()

    @app.exception_handler(BaseError)
    async def custom_error_handler(req: Request, exc: BaseError):
        """
        Catches custom errors that inherit from BaseError
        Returns status_code + error code + custom message
        """
        return exc.to_response()

    @app.exception_handler(Exception)
    async def generic_exception_handler(req: Request, exc: Exception):
        # Catches unexpected errors and returns a generic message
        return BaseError(
            status=500, message='Internal Server Error.', code='INTERNAL_SERVER_ERROR'
        )
