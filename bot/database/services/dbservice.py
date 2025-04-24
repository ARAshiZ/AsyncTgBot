from sqlalchemy import select
from bot.database import User, Employee


class DatabaseService:

    def __init__(self, session_maker):
        self.session = session_maker

    async def check_exists_users(self, tg_id):
        async with self.session() as db:
            result = await db.execute(select(User).where(User.tg_id == tg_id))
            return result.scalar_one_or_none() is not None

    async def exists_users(self):
        async with self.session() as db:
            result = await db.execute(select(User))
            return result.scalars().all()

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

    async def insert_employee(self, user_id, offer, date):
        async with self.session() as db:
            try:
                existing_user = await db.get(User, user_id)
                new_employee = Employee(user_id=existing_user.user_id, employee_offer=offer, employee_date=date)
                db.add(new_employee)
                await db.commit()
            except Exception as e:
                await db.rollback()
                raise e
            finally:
                await db.close()