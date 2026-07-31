from pydantic import BaseModel, EmailStr


class UserDTORes(BaseModel):
    id: int
    name: str
    email: EmailStr
    access_token: str
    refresh_token: str
    token_type: str