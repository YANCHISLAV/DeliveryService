from datetime import datetime

from pydantic import Field, BaseModel


class CommentDTOReq(BaseModel):

    user_id: int = Field(ge=0)
    restaurant_id: int = Field(ge=0)
    text: str | None = None
    rate: float = Field(ge=0)
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)