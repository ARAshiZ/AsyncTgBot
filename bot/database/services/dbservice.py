
from aiogram.types import Message

from sqlalchemy import select, inspect
from sqlalchemy.ext.asyncio import AsyncEngine

from bot.database import User, Employee, Job, About, Subscribe
from bot.misc import redis


class DatabaseService:

    def __init__(self, session_maker):
        self.session = session_maker

    async def is_user_exists(self, tg_id):
        async with self.session() as db:
            result = await redis.get(name=str(tg_id))
            if not result:
                return bool(result)
            else:
                return bool(result)

    async def exists_users(self):
        async with self.session() as db:
            result = await db.execute(select(User))
            return result.scalars().all()

    async def insert_user(self, name, date, tg_id):
        async with self.session() as db:
            try:
                new_user = User(user_name=name, reg_date=date, tg_id=tg_id)
                db.add(new_user)
                await redis.set(name=str(tg_id), value=1)
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

    async def insert_job(self, title, payment, high_edu):
        async with self.session() as db:
            try:
                new_job = Job(job_title=title, job_pay=payment, job_have_high_education=high_edu)
                db.add(new_job)
                await db.commit()
            except Exception as e:
                await db.rollback()
                raise e
            finally:
                await db.close()

    async def insert_about(self, title, info, date):
        async with self.session() as db:
            try:
                new_about = About(model_title=title, information=info, info_create_date=date)
                db.add(new_about)
                await db.commit()
            except Exception as e:
                await db.rollback()
                raise e
            finally:
                await db.close()

    async def insert_subscribe(self, title, date, price):
        async with self.session() as db:
            try:
                new_subscribe = Subscribe(subscribe_title=title, subscribe_term=date, subscribe_price=price)
                db.add(new_subscribe)
                await db.commit()
            except Exception as e:
                await db.rollback()
                raise e
            finally:
                await db.close()

    async def get_table_names(self):
        return list(User.metadata.tables.keys())
