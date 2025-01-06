from fastapi import (
    APIRouter,
    Depends,
)
from sqlalchemy.ext.asyncio import AsyncSession

from app.utilities.tron import get_tron_info
from app.core.db import get_async_session
from app.crud import history_crud
from app.schemas import (
    DefaultPagination,
    BasePaginatedResponse,
    HistoryCreate,
    HistoryCreateDB,
    HistoryResponse,
)


router = APIRouter()


@router.get('/', response_model=BasePaginatedResponse)
async def get_hist(
    session: AsyncSession = Depends(get_async_session),
    pagination: DefaultPagination = Depends(),
):
    return await history_crud.get_multi(
        session=session, pagination=pagination
    )


@router.post('/', response_model=HistoryResponse)
async def create_hist(
    data: HistoryCreate,
    session: AsyncSession = Depends(get_async_session),
):
    new_data = dict.fromkeys(['request', 'answer'])
    new_data['request'] = data.request
    new_data['answer'] = await get_tron_info(data.request)
    return await history_crud.create(
        session=session, obj_in=HistoryCreateDB(**new_data))
