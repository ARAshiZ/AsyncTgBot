import os
import asyncio
import logging
import sys
from aiogram import Dispatcher, Bot
from aiogram.types import BotCommand
from commands import register_user_commands
from commands.constants import bot_commands

async def main() -> None:
    commands_for_bot = []
    for cmd in bot_commands:
        commands_for_bot.append(BotCommand(command=cmd[0], description=cmd[1]))
    dp = Dispatcher()
    bot = Bot(token=os.getenv('token'))

    await bot.set_my_commands(commands=commands_for_bot)
    register_user_commands(dp)
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        logging.basicConfig(level=logging.INFO, stream=sys.stdout)
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print('bot stopped')
