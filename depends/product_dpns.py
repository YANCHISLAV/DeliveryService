from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from infrastructure.db.session import db
from infrastructure.products.sqlalchemy_p_repository import SQLAlchemyProductRepository
from use_cases.products.p_service import ProductService


async def product_service_provider(session: AsyncSession = Depends(db.get_session))->ProductService:
    p_repo = SQLAlchemyProductRepository(session=session)
    return ProductService(product_repo=p_repo)