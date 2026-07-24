from datetime import datetime

from pydantic import BaseModel, Field, ConfigDict

from domain.enums.order_status import OrderStatus


class Order(BaseModel):
    id: int | None = None
    user_id: int = Field(ge=0)
    discount: float = Field(ge=0)
    created_at: datetime
    status: OrderStatus

    model_config = ConfigDict(from_attributes=True)