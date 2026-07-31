from pydantic import BaseModel, EmailStr


class GetUserDTOOut(BaseModel):
    id: int
    name: str
    email: EmailStr