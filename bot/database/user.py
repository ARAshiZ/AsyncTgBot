import datetime

from sqlalchemy import Column, VARCHAR, INTEGER, DATE
from sqlalchemy.orm import relationship

from .base import BaseModel

class User(BaseModel):
    __tablename__ = 'users'
    
    user_id = Column(INTEGER, primary_key=True, unique=True, nullable=False, autoincrement=True)
    user_name = Column(VARCHAR(20), unique=False, nullable=True)
    reg_date = Column(DATE, default=datetime.date.today())
    tg_id = Column(INTEGER, unique=True)
    employees = relationship("Employee", back_populates="user")
