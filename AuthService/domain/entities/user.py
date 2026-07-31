from pydantic import BaseModel, EmailStr, Field, ConfigDict

from domain.enums.user_roles import UserRoles


class User(BaseModel):
    id: int
    name: str
    role: UserRoles
    email: EmailStr
    password: str = Field(min_length=8, max_length=64)

    model_config = ConfigDict(from_attributes=True)