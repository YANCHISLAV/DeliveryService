from pydantic import BaseModel, EmailStr, Field

class User(BaseModel):
    id : int = Field(ge = 0)
    username: str = Field(max_length = 100)
    email: EmailStr
    password: str = Field(max_length = 100)
