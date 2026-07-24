from pydantic import BaseModel, Field, ConfigDict

from domain.entities.product import Product
from domain.enums.cuisines import Cuisine


class Restaurant(BaseModel):
    id: int | None = None
    name: str = Field(max_length=40)
    city: str = Field(max_length=50)
    street: str = Field(max_length=50)
    house_number: int = Field(gt=0)
    working_days: dict
    description: str = Field(max_length=200)
    menu: list[Product]
    rate: float = Field(ge=0)
    cuisines: list[Cuisine]

    model_config = ConfigDict(from_attributes=True)