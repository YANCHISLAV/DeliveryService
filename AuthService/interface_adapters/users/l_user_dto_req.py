from pydantic import BaseModel, Field, EmailStr

class LoginUserDTOReq(BaseModel):
    email: EmailStr = Field(max_length=50)
    password: str = Field(min_length=8, max_length=64)