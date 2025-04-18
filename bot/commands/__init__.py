__all__ = ['start']

from aiogram import Router
from aiogram.filters import CommandStart

from bot.commands.start import start_command


def register_user_commands(router: Router) -> None:
    router.message.register(start_command, CommandStart)