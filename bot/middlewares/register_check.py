import datetime
from cgitb import handler
from typing import Callable, Dict, Any, Awaitable
from aiogram import BaseMiddleware
from aiogram.types import Message
from sqlalchemy import select, Result
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker

from bot.database import User
from bot.database.services.dbservice import DatabaseService


class RegisterCheck(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str, Any],
    ) -> Any:
        try:
            service = data['service']
            user_name = event.from_user.username
            user_tg_id = event.from_user.id
            reg_date = datetime.date.today()
            await service.insert_user(user_name, reg_date, user_tg_id)
            await event.answer('Пользователь добавлен!')
        except Exception as e:
            await event.answer('Не удалось создать пользователя')
            raise e
        return await handler(event, data)
