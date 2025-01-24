__all__ = ['register_user_commands']

from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram import F

from bot.commands.download import download_command
from bot.commands.help import help_command, call_help
from bot.commands.keyboard import create_menu, bring_to_main
from bot.commands.sticker import sticker_command, call_sticker
from bot.commands.upload import upload_command


def register_user_commands(router: Router) -> None:

    router.message.register(create_menu, CommandStart())
    router.message.register(help_command, Command(commands=['help']))
    router.message.register(download_command, Command(commands=['download']),
                            F.content_type.in_({'photo', 'video', 'audio', 'text'}))
    router.message.register(upload_command, Command(commands=['upload']),
                            F.content_type.in_({'photo', 'video', 'audio', 'text'}))
    router.message.register(sticker_command, Command(commands=['sticker']))

    router.callback_query.register(bring_to_main, F.data == 'back')
    router.callback_query.register(call_help, F.data == 'help')
    router.callback_query.register(call_sticker, F.data == 'sticker')
