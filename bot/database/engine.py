from sqlalchemy.engine import URL
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from .base import BaseModel

class EngineDB:
    def __init__(self, driver, username, password, host, port, db_name):
        self.engine = None
        self.mysql_url = URL.create(
            drivername=driver,
            username=username,
            password=password,
            host=host,
            port=port,
            database=db_name
        )
        
    async def run_engine(self):
        self.engine = create_async_engine(
            self.mysql_url,
            echo=True
        )
        async with self.engine.begin() as conn:
            await conn.run_sync(BaseModel.metadata.create_all)
            
    def get_session_maker(self):
        return sessionmaker(self.engine, class_=AsyncSession)