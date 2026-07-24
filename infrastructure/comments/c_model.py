from datetime import datetime

from sqlalchemy import Integer, ForeignKey, String, DateTime, Float
from sqlalchemy.orm import Mapped, mapped_column

from infrastructure.db.base_model import Base


class CommentModel(Base):

    __tablename__ = 'comment'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey('user.id'), unique=True)
    restaurant_id: Mapped[int] = mapped_column(Integer, unique=True) #добавить foreign key
    text: Mapped[str] = mapped_column(String(200))
    rate: Mapped[float] = mapped_column(Float)
    created_at: Mapped[datetime] = mapped_column(DateTime)
    updated_at: Mapped[datetime] = mapped_column(DateTime)
