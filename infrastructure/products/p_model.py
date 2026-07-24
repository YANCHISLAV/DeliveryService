from sqlalchemy import Integer, String, Float, Enum, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from domain.enums.categories import Category
from domain.enums.cuisines import Cuisine
from infrastructure.db.base_model import Base


class ProductModel(Base):
    __tablename__ = 'product'
    id : Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    restaurant_id: Mapped[int] = mapped_column(Integer, ForeignKey('restaurant.id'), unique=True)
    name: Mapped[str] = mapped_column(String(50), unique=True)
    price: Mapped[float] = mapped_column(Float,  default=0.0)
    weight: Mapped[float] = mapped_column(Float, default=0.0)
    quantity: Mapped[int] = mapped_column(Integer, default=0)
    description: Mapped[str] = mapped_column(String(200))
    category: Mapped[Category] = mapped_column(Enum(Category, native_enum=False))
    cuisine: Mapped[Cuisine] = mapped_column(Enum(Cuisine, native_enum=False))