from pydantic import BaseModel, EmailStr

class LoginUserDTOInp(BaseModel):
    email: EmailStr
    password: str
