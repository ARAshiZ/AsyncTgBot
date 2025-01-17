import os
from aiogram import types, Bot
from aiogram.filters import CommandObject
from aiogram.types import InputFile, FSInputFile

from bot.commands.constants import save_dir_path

async def upload_command(message: types.Message, command: CommandObject, bot: Bot):
    files = [f for f in os.listdir(save_dir_path) if os.path.isfile(os.path.join(save_dir_path, f))]

    for file_name in files:
        file_path = os.path.join(save_dir_path, file_name)

        if command.args == 'photo':
            if file_name.endswith(".jpg"):
                video_file = FSInputFile(file_path)
                await message.answer_photo(photo=video_file)
        elif command.args == 'video':
            if file_name.endswith(".mp4"):
                video_file = FSInputFile(file_path)
                await message.answer_video(video=video_file)
        elif command.args == 'audio':
            if file_name.endswith(".mp3"):
                video_file = FSInputFile(file_path)
                await message.answer_audio(audio=video_file)
        else:
            await message.answer('Данного файла не существует')
            return