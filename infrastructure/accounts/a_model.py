
from sqlalchemy import ForeignKey, Integer, Float
from sqlalchemy.orm import Mapped, mapped_column, relationship

from infrastructure.db.base_model import Base

class AccountModel(Base):
    __tablename__ = 'account'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    wallet_id: Mapped[int] = mapped_column(ForeignKey('wallet.id'), unique=True)
    amount: Mapped[float] = mapped_column(Float, default=0.0)
