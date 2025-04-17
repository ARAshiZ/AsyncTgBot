import datetime

from sqlalchemy import Column, VARCHAR, INTEGER, DATE
from .base import BaseModel

class User(BaseModel):
    __tablename__ = 'users'
    
    user_id = Column(INTEGER, primary_key=True, unique=True, nullable=False, autoincrement=True)
    user_name = Column(VARCHAR(20), unique=False, nullable=True)
    reg_date = Column(DATE, default=datetime.date.today())
    update_date = Column(DATE, default=datetime.date.today())
    
    def __str__(self) -> str:
        return f'user: {self.user_id}'