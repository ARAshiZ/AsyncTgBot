from sqlalchemy import select
from sqlalchemy.orm import Session

from bot.database import engine, User


class DatabaseService:

    def __init__(self, session_maker):
        self.session = session_maker

    async def check_exists_users(self, tg_id):
        async with self.session() as db:
            result = await db.execute(select(User).where(User.tg_id == tg_id))
            return result.scalar_one_or_none() is not None


    async def insert_user(self, name, date, tg_id):
        async with self.session() as db:
            try:
                exists = await self.check_exists_users(tg_id)
                if exists:
                    return
                new_user = User(user_name=name, reg_date=date, tg_id=tg_id)
                db.add(new_user)
                await db.commit()
            except Exception as e:
                await db.rollback()
                raise e
            finally:
                await db.close()