from aiogram.types import Message, FSInputFile
from aiogram import Bot
import random
import os
import requests

directory = 'D:/Institute/Programming/Laboratory work/third_course/TelegramBot/Audio'  # Замените на путь к вашей директории

files = os.listdir(directory)

files = [file for file in files if os.path.isfile(os.path.join(directory, file))]

async def get_audio(message: Message, bot: Bot):
    random_file = random.choice(files)
    audio = FSInputFile(path=str(directory) + '/' + str(random_file), filename=random_file)
    await bot.send_audio(message.chat.id, audio=audio)

async def get_photo(message: Message, bot: Bot):
    image_url = 'https://randomfox.ca/images/' + str(random.randint(1, 120)) + '.jpg'
    response = requests.get(image_url)
    if response.status_code == 200:
        image_filename = os.path.basename(image_url)
        with open(image_filename, 'wb') as image_file:
            image_file.write(response.content)
            image = FSInputFile(path=image_filename)
            await bot.send_photo(message.chat.id, photo=image)

        os.remove(image_filename)
    else:
        await message.reply("Не удалось загрузить изображение по указанной ссылке. Попробуйте снова.")