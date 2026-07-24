from datetime import datetime

from pydantic import BaseModel, Field, ConfigDict


class Account(BaseModel):
    id: int | None = None
    wallet_id: int = Field(ge=0)
    account_number: str = Field(min_length=16, max_length=16)
    updated_at: datetime
    amount: float = Field(ge=0)

    model_config = ConfigDict(from_attributes=True)