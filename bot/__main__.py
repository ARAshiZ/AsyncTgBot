import os
import asyncio
import logging
import sys

from aiogram import Dispatcher, Bot
from aiogram.types import BotCommand
from bot.commands import register_user_commands
from bot.commands.constants import bot_commands
from bot.database import EngineDB
from bot.database.dbmiddleware import DbMiddleware
from bot.database.services.dbservice import DatabaseService


async def main() -> None:
    commands_for_bot = []
    for cmd in bot_commands:
        commands_for_bot.append(BotCommand(command=cmd[0], description=cmd[1]))
    dp = Dispatcher()
    bot = Bot(token=os.getenv('token'))

    await bot.set_my_commands(commands=commands_for_bot)
    register_user_commands(dp)
    start_conn = EngineDB(
        driver='postgresql+asyncpg',
        username='postgres',
        password='5371',
        host='localhost',
        port=5432,
        db_name='tgbot'
    )
    await start_conn.run_engine()
    Session = start_conn.get_session_maker()
    service = DatabaseService(Session)
    dp['service'] = service
    dp.update.outer_middleware(DbMiddleware())
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        logging.basicConfig(level=logging.INFO, stream=sys.stdout)
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print('bot stopped')
