from sqlalchemy import Integer, String, Enum
from sqlalchemy.orm import Mapped, mapped_column

from domain.enums.user_roles import UserRoles
from infrastructure.db.base_model import Base


class UserModel(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    role: Mapped[UserRoles] = mapped_column(Enum(UserRoles, native_enum=False), default=UserRoles.USER)
    name: Mapped[str] = mapped_column(String(50), unique=True)
    email: Mapped[str] = mapped_column(String(50), unique=True)
    password: Mapped[str] = mapped_column(String(50))