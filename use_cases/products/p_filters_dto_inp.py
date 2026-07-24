from pydantic import BaseModel

from domain.enums.categories import Category
from domain.enums.cuisines import Cuisine


class ProductFiltersDTOInp(BaseModel):
    name: str | None
    min_price: float | None
    max_price: float | None
    category: Category | None
    cuisine: Cuisine | None

