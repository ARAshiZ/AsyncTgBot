import os
import asyncio
import logging
import sys

from aiogram import Dispatcher, Bot
from aiogram.fsm.storage.redis import RedisStorage
from aiogram.types import BotCommand

from commands import register_user_commands
from commands.constants import bot_commands
from database import EngineDB
from database.dbmiddleware import DbMiddleware
from database.services.dbservice import DatabaseService
from middlewares.register_check import RegisterCheck
from misc import redis


async def main() -> None:
    commands_for_bot = []
    for cmd in bot_commands:
        commands_for_bot.append(BotCommand(command=cmd[0], description=cmd[1]))
    dp = Dispatcher(storage=RedisStorage(redis=redis))
    bot = Bot(token=os.getenv('token'))

    await bot.set_my_commands(commands=commands_for_bot)
    register_user_commands(dp)
    start_conn = EngineDB(
        driver='postgresql+asyncpg',
        username='postgres',
        password='5371',
        host='host.docker.internal',
        port=5432,
        db_name='tgbot'
    )
    await start_conn.run_engine()
    Session = start_conn.get_session_maker()
    service = DatabaseService(Session)
    dp['service'] = service
    dp.message.middleware(RegisterCheck())
    dp.callback_query.middleware(RegisterCheck())
    dp.update.outer_middleware(DbMiddleware())
    await dp.start_polling(bot, session_maker=Session)

if __name__ == '__main__':
    try:
        logging.basicConfig(level=logging.INFO, stream=sys.stdout)
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print('bot stopped')
