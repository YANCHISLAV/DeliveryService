from datetime import datetime

from pydantic import Field, BaseModel


class CommentDTOInp(BaseModel):

    user_id: int = Field(ge=0)
    restaurant_id: int = Field(ge=0)
    text: str | None
    rate: float = Field(ge=0)
    created_at: datetime
    updated_at: datetime