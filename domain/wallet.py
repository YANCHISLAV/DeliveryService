from pydantic import BaseModel, Field

class Wallet(BaseModel):
    id: int = Field(ge=0)
    amount: float = Field(ge=0)
