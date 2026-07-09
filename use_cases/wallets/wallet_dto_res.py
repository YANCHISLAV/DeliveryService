from pydantic import BaseModel, Field

class WalletDTORes(BaseModel):
    id: int = Field(ge=0)
    amount: int = Field(ge=0)