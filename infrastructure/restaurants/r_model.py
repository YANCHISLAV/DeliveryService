from typing import Any

from sqlalchemy import Integer, String, CheckConstraint, Float
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column

from domain.enums.cuisines import Cuisine
from infrastructure.db import Base


class RestaurantModel(Base):
    __tablename__ = 'restaurant'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(50))
    city: Mapped[str] = mapped_column(String(50))
    street: Mapped[str] = mapped_column(String(50))
    house_number:Mapped[int] = mapped_column(Integer)
    working_days:Mapped[dict[str, Any]] = mapped_column(JSONB)
    description: Mapped[str] = mapped_column(String(200))
    rate: Mapped[float] = mapped_column(Float)
    cuisines: Mapped[list[Cuisine]] = mapped_column(JSONB)

    __table_args__ = (CheckConstraint('house_number>0'),)