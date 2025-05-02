import datetime
from email.policy import default

from sqlalchemy import Column, VARCHAR, INTEGER, DATE, ForeignKey
from sqlalchemy.dialects.mysql import NUMERIC

from .base import BaseModel


class About(BaseModel):
    __tablename__ = 'about'

    about_id = Column(INTEGER, primary_key=True, autoincrement=True, unique=True, nullable=False)
    model_title = Column(VARCHAR(20), default='')
    information = Column(VARCHAR(200), default='')
    info_create_date = Column(DATE, default=datetime.date.today())
