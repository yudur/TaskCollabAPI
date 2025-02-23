from typing import Dict, List, Optional

from fastapi.responses import JSONResponse

from taskcollabapi.schemas.responses import ErrorResponseSchema


class BaseError(Exception):
    def __init__(
        self,
        status: int,
        message: str,
        code: str,
        data: Optional[List | Dict | None] = None,
    ):
        self.status = status
        self.message = message
        self.code = code
        self.data = data

    def to_response(self):
        content = ErrorResponseSchema(
            status=self.status, code=self.code, message=self.message, data=self.data
        )

        # only returns fields that are different from "None"
        return JSONResponse(
            status_code=self.status, content=content.model_dump(exclude_unset=True)
        )
