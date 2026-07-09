
from pydantic import BaseModel, Field

class WalletDTOReq(BaseModel):
    user_id: int = Field(ge=0)
