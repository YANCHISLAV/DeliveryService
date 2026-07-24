from pydantic import BaseModel, Field

class AccountDTOOut(BaseModel):
    id: int = Field(ge=0)
    wallet_id: int = Field(ge=0)
    amount: float = Field(ge=0)