from datetime import datetime

from pydantic import BaseModel, Field

from domain.enums.transaction_status import TransactionStatus


class TransactionDTOInp(BaseModel):
    account_id: int = Field(ge=0)
    amount: float = Field(ge=0)
    created_at: datetime = Field(default_factory=datetime.now)
    status: TransactionStatus = Field(default=TransactionStatus.Pending)