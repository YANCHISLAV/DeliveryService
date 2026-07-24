from domain.exceptions.base_exceptions import ModelAlreadyExistException, ModelNotExistException
from use_cases.comments.c_dto_inp import CommentDTOInp
from use_cases.comments.c_dto_out import CommentDTOOut


class CommentService:
    def __init__(self, comment_repo):
        self.comment_repo = comment_repo

    async def get_by_id(self, comment_id) -> CommentDTOOut:
        c_out = await self.comment_repo.get_by_id(comment_id)
        if not c_out:
            raise ModelNotExistException("comment")
        return CommentDTOOut(**c_out.model_dump())

    async def create(self, comment: CommentDTOInp) -> CommentDTOOut:
        try:
            await self.comment_repo.create(comment)
        except ModelNotExistException("comment"):
            c_out = await self.comment_repo.create(comment)
            return CommentDTOOut(**c_out.model_dump())
        raise ModelAlreadyExistException("comment")
