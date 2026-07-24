from datetime import datetime

from pydantic import Field, BaseModel


class CommentDTORes(BaseModel):

    id: int = Field(ge=0)
    user_id: int = Field(ge=0)
    restaurant_id: int = Field(ge=0)
    text: str | None
    rate: float = Field(ge=0)
    created_at: datetime
    updated_at: datetime