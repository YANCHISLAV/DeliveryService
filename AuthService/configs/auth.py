from pydantic import BaseModel


class AuthConfig(BaseModel):
    secret_key: str
    algorithm: str = 'HS256'