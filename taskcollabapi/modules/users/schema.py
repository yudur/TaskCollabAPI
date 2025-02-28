from typing import Literal, Optional

from pydantic import BaseModel, EmailStr


class UserCreateSchema(BaseModel):
    name: str
    email: EmailStr
    password: str
    role: Optional[Literal['ADMIN', 'COLLABORATOR', 'VISITOR']] = 'VISITOR'
