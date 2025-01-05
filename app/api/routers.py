from fastapi import (
    APIRouter,
    Depends,
    status,
    HTTPException,
)
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.crud import history_crud
from app.schemas import DefaultPagination, BasePaginatedResponse


router = APIRouter()


@router.get('/', response_model=BasePaginatedResponse)
async def tab(
    session: AsyncSession = Depends(get_async_session),
    pagination: DefaultPagination = Depends(),
):
    return await history_crud.get_multi(
        session=session, pagination=pagination
    )