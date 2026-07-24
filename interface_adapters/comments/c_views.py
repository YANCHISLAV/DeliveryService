
from fastapi import APIRouter

from interface_adapters.comments.c_dto_req import CommentDTOReq
from use_cases.comments.c_service import CommentService

router = APIRouter(prefix="/comments", tags=["comments"])

@router.get("/{c_id}")
async def get_by_id(c_id: int):
    pass

@router.post("/")
async def create(comment : CommentDTOReq, comment_service: CommentService):
    pass