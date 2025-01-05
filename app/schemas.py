from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel, Extra


class HistoryBase(BaseModel):
    request: str

    class Config:
        from_attributes = True


class HistoryCreate(HistoryBase):

    class Config:
        extra = Extra.forbid


class HistoryCreateDB(HistoryCreate):
    answer: str


class HistoryResponse(HistoryCreateDB):
    id: int
    datetime: datetime


class DefaultPagination(BaseModel):
    limit: int = 20
    skip: int = 0


class BasePaginatedResponse(BaseModel):
    limit: Optional[int]
    offset: Optional[int]
    total: Optional[int]
    objects: List[HistoryResponse]

    class Config:
        arbitrary_types_allowed = True
