from pydantic import BaseModel, Field


class AccountDTOInp(BaseModel):
    wallet_id: int = Field(ge=0)
    amount: float = Field(default=0.0)