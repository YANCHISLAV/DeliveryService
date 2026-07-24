from datetime import datetime
from pydantic import BaseModel, Field

from domain.enums.order_status import OrderStatus


class OrderDTOInp(BaseModel):
    user_id: int = Field(ge=0)
    # products: list[Product]
    discount: float = Field(ge=0)
    created_at: datetime
    status: OrderStatus

