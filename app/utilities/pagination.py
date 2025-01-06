from typing import Dict, Sequence
from sqlalchemy import RowMapping

from app.schemas import DefaultPagination


async def get_paginated(
    pagination: DefaultPagination,
    objects: Sequence[RowMapping],
) -> Dict:
    return {
        'limit': pagination.limit,
        'offset': pagination.skip,
        'objects': [o for o in objects],
    }
