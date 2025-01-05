from datetime import datetime
from sqlalchemy import Column, String, DateTime

from app.core.db import Base


class History(Base):
    datetime = Column(DateTime, default=datetime.now)
    request = Column(String, nullable=False, comment='Запрос')
    answer = Column(String, comment='Ответ на запрос')
