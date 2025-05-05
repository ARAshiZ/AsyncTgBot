import os
from aiogram import types, Bot
from commands.constants import save_dir_path


async def download_command(message: types.Message, bot: Bot):
    if message.photo:
        file_id = message.photo[-1].file_id
        file_type = "photo"
        file_extension = ".jpg"
    elif message.video:
        file_id = message.video.file_id
        file_type = "video"
        file_extension = ".mp4"
    elif message.audio:
        file_id = message.audio.file_id
        file_type = "audio"
        file_extension = ".mp3"
    else:
        await message.answer("Медиафайл не распознан")
        return

    delete_exist(file_extension)
    file = await bot.get_file(file_id)
    file_path = file.file_path
    await bot.download_file(file_path,
                            f"{save_dir_path}{file_type}_{file_id}{file_extension}")
    return await message.answer(f"Файл типа {file_type} успешно скачан!")

def delete_exist(file_extension):
    directory_path = save_dir_path
    try:
        items = os.listdir(directory_path)
        files = [item for item in items if os.path.isfile(os.path.join(directory_path, item))]
        for file_name in files:
            after_separator = file_name.split(".", maxsplit=1)[-1]
            if "." + after_separator == file_extension:
                file_path = os.path.join(save_dir_path, file_name)
                os.remove(file_path)

    except FileNotFoundError:
        print(f"Директория {directory_path} не найдена.")
    except Exception as e:
        print(f"Ошибка при получении списка файлов: {e}")