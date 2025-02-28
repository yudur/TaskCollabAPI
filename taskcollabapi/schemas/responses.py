from typing import Dict, List, Optional

from pydantic import BaseModel, ConfigDict


class BaseResponseSchema(BaseModel):
    """
    generic response class.

    where it will be used to show the parameters that are mandatory from route to route.

    This class should not be called directly but rather by inheritance.

    - status: HTTP error code (e.g. 400, 404, 500)
    - code: Error identifier code (e.g. 'USER_NOT_FOUND')
    - message: Descriptive error message
    - ...: additional fields
    """

    status: int
    code: str
    message: str

    model_config = ConfigDict(extra='allow')


class ErrorResponseSchema(BaseResponseSchema):
    data: Optional[Dict | List] = None
