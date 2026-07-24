from pydantic import BaseModel, Field

from domain.enums.cuisines import Cuisine


class RestaurantDTORes(BaseModel):
    id: int = Field(ge=0)
    name: str = Field(max_length=40)
    city: str = Field(max_length=50)
    street: str = Field(max_length=50)
    house_number: int = Field(gt=0)
    working_days: dict
    description: str = Field(max_length=200)
    rate: float = Field(ge=0)
    cuisines: list[Cuisine]
