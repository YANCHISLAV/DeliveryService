from pydantic import BaseModel

from domain.enums.categories import Category
from domain.enums.cuisines import Cuisine


class ProductFiltersDTOReq(BaseModel):
    name: str | None = None
    min_price: float | None = None
    max_price: float | None = None
    category: Category | None = None
    cuisine: Cuisine | None = None
