from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from domain.entities.comment import Comment
from infrastructure.comments.c_model import CommentModel
from use_cases.comments.c_repo_interface import CommentRepoInterface


class SQLAlchemyCommentRepository(CommentRepoInterface):

    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, comment: Comment) -> Comment:
        model = CommentModel(**comment.model_dump())
        self.session.add(model)
        await self.session.flush()
        await self.session.refresh(model)
        return Comment.model_validate(model)

    async def get_by_id(self, comment_id: int) -> Comment:
        query = select(CommentModel).where(CommentModel.id == comment_id)
        query_res = await self.session.execute(query)
        comment = await query_res.scalar()
        return Comment.model_validate(comment)