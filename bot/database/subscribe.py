import datetime

from sqlalchemy import Column, VARCHAR, INTEGER, DATE
from sqlalchemy.dialects.mysql import NUMERIC

from .base import BaseModel


class Subscribe(BaseModel):
    __tablename__ = 'subscribes'

    subscribe_id = Column(INTEGER, primary_key=True, unique=True, nullable=False, autoincrement=True)
    subscribe_title = Column(VARCHAR(20), unique=False, nullable=True)
    subscribe_term = Column(DATE, default='')
    subscribe_price = Column(NUMERIC(10, 2), default=0.00)