from datetime import datetime

from pydantic import BaseModel, Field

from domain.enums.order_status import OrderStatus


class OrderDTORes(BaseModel):
    id: int = Field(ge=0)
    user_id: int = Field(ge=0)
    # products
    discount: float = Field(ge=0)
    created_at: datetime
    status: OrderStatus
