__all__ = ['register_user_commands']

from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram import F

from bot.commands.download import download_command
from bot.commands.start import start_command
from bot.commands.help import help_command
from bot.commands.upload import upload_command


def register_user_commands(router: Router) -> None:
    router.message.register(start_command, CommandStart())
    router.message.register(help_command, Command(commands=['help']))
    router.message.register(download_command, Command(commands=['download']),
                            F.content_type.in_({'photo', 'video', 'audio', 'text'}))
    router.message.register(upload_command, Command(commands=['upload']),
                            F.content_type.in_({'photo', 'video', 'audio', 'text'}))