import datetime
from email.policy import default

from sqlalchemy import Column, VARCHAR, INTEGER, DATE, ForeignKey
from sqlalchemy.dialects.mysql import NUMERIC
from sqlalchemy.orm import relationship

from .base import BaseModel


class Employee(BaseModel):
    __tablename__ = 'employees'

    employee_id = Column(INTEGER, primary_key=True, autoincrement=True, unique=True, nullable=False)
    user_id = Column(INTEGER, ForeignKey('users.user_id'))
    employee_offer = Column(VARCHAR(20), default='intern')
    employee_date = Column(DATE, default='')
    user = relationship("User", back_populates="employees")