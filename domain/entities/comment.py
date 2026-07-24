from datetime import datetime

from pydantic import BaseModel, Field


class Comment(BaseModel):

    id: int | None
    user_id: int = Field(ge=0)
    restaurant_id: int = Field(ge=0)
    text: str | None
    rate: float
    created_at: datetime
    updated_at: datetime
