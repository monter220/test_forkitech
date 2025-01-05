from typing import Dict, Sequence, Type
from sqlalchemy import RowMapping

from app.core.db import Base
from app.schemas import DefaultPagination


async def get_paginated(
    pagination: DefaultPagination,
    objects: Sequence[RowMapping],
    model: Type[Base],
) -> Dict:
    return {
        'limit': pagination.limit,
        'offset': pagination.skip,
        'total': objects[0]['total_count'] if objects else 0,
        'objects': [o[model.__name__] for o in objects],
    }
