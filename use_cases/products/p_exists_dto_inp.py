from pydantic import BaseModel


class ProductExistsDTOInp(BaseModel):
    restaurant_id: int
    name: str