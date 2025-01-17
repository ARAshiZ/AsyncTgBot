from aiogram import types, Bot


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

    file = await bot.get_file(file_id)
    file_path = file.file_path
    await bot.download_file(file_path,
                            f"C:/Users/Danya/PycharmProjects/AsyncTgBot/bot/downloads/{file_type}_{file_id}{file_extension}")
    return await message.answer(f"Файл типа {file_type} успешно скачан!")
