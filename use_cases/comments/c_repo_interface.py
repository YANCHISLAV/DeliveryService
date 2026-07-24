
from abc import ABC, abstractmethod

from domain.entities.comment import Comment


class CommentRepoInterface(ABC):

    @abstractmethod
    async def create(self, comment)->Comment:
        pass

    async def get_by_id(self, comment_id) -> Comment:
        pass