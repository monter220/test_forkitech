from typing import List
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


class HistoryResponse(HistoryBase):
    id: int
    datetime: datetime
    answer: str

    class Config:
        orm_mode = True


class DefaultPagination(BaseModel):
    limit: int = 20
    skip: int = 0


class BasePaginatedResponse(BaseModel):
    limit: int
    offset: int
    objects: List[HistoryResponse]

    class Config:
        arbitrary_types_allowed = True
