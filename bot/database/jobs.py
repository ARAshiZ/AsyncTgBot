import datetime
from email.policy import default

from sqlalchemy import Column, VARCHAR, INTEGER, DATE, ForeignKey, BOOLEAN
from sqlalchemy.dialects.mysql import NUMERIC

from .base import BaseModel


class Job(BaseModel):
    __tablename__ = 'jobs'

    job_id = Column(INTEGER, primary_key=True, autoincrement=True, unique=True, nullable=False)
    job_title = Column(VARCHAR(20), default='')
    job_pay = Column(NUMERIC(10,2), default=0.00)
    job_have_highedu = Column(BOOLEAN, default=False)


