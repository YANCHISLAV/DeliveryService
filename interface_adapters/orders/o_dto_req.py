from datetime import datetime

from pydantic import BaseModel, Field

from domain.enums.order_status import OrderStatus


class OrderDTOReq(BaseModel):
    user_id: int = Field(ge=0)
    # products
    discount: float = Field(ge=0)
    created_at: datetime = Field(default_factory=datetime.now)
    status: OrderStatus = Field(default=OrderStatus.CREATED)
