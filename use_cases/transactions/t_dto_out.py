from datetime import datetime
from pydantic import BaseModel, Field

from domain.enums.transaction_status import TransactionStatus


class TransactionDTOOut(BaseModel):
    id: int = Field(ge=0)
    account_id: int = Field(ge=0)
    amount: float = Field(ge=0)
    created_at: datetime
    status: TransactionStatus