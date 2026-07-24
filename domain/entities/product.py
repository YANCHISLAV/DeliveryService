from pydantic import BaseModel, Field, ConfigDict
from domain.enums.categories import Category
from domain.enums.cuisines import Cuisine


class Product(BaseModel):
    id: int | None = None
    restaurant_id: int = Field(ge=0)
    name: str = Field(max_length=100)
    price: float = Field(ge=0)
    weight: float = Field(gt=0)
    quantity: int = Field(ge=0)
    description: str = Field(max_length=500)
    category: Category
    cuisine: Cuisine

    model_config = ConfigDict(from_attributes=True)