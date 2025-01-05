from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import History
from app.schemas import DefaultPagination
from app.utilities.pagination import get_paginated


class CRUDBase:

    def __init__(self, model):
        self.model = model

    async def get_multi(
            self,
            session: AsyncSession,
            pagination: DefaultPagination,
    ):
        statement = (
            select(self.model)
            .offset(pagination.skip)
            .limit(pagination.limit)
        )
        db_objs = await session.execute(statement)
        objects = db_objs.scalars().all()
        return await get_paginated(
            objects=objects, model=self.model, pagination=pagination)

    async def create(
            self,
            obj_in,
            session: AsyncSession,
    ):
        obj_in_data = obj_in.dict()
        db_obj = self.model(**obj_in_data)
        session.add(db_obj)
        await session.commit()
        await session.refresh(db_obj)
        return db_obj


history_crud = CRUDBase(History)
