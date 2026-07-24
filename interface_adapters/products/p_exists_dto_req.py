from pydantic import BaseModel, Field


class ProductExistsDTOReq(BaseModel):
    restaurant_id: int = Field(ge=0)
    name: str = Field(max_length=50)