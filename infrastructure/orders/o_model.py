from datetime import datetime

from sqlalchemy import DateTime, Integer, Float, Enum
from sqlalchemy.orm import mapped_column, Mapped

from domain.enums.order_status import OrderStatus
from infrastructure.db.base_model import Base

class OrderModel(Base):
    __tablename__ = "orders"
    id : Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id : Mapped[int] = mapped_column(Integer,unique=True)
    discount : Mapped[float] = mapped_column(Float, default=0.0)
    created_at: Mapped[datetime] = mapped_column(DateTime)
    status: Mapped[OrderStatus] = mapped_column(Enum(OrderStatus, native_enum=False))