from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from core.handlers.basic import get_start, get_hello, get_info, get_git, stop
from core.handlers.send_media import get_audio, get_photo
import asyncio
import logging
from core.settings import settings
from aiogram.filters import Command
from aiogram import F
from core.utils.commands import set_commands
from core.keyboards.reply import reply_keyboard

async def start_bot(bot: Bot):
    await set_commands(bot)
    await bot.send_message(settings.bots.admin_id, text='Working.')

async def stop_bot(bot: Bot):
    await bot.send_message(settings.bots.admin_id, text='Stop working.')

async def start():
    logging.basicConfig(level=logging.INFO)

    bot = Bot(token=settings.bots.bot_token, parse_mode='HTML')
    
    dp = Dispatcher()
    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)

    dp.message.register(get_hello, F.text == 'Привет')

    dp.message.register(get_start, Command(commands=['start', 'run']))
    dp.message.register(get_info, Command(commands=['info', 'information']))

    dp.message.register(get_audio, Command(commands=['get_audio']))
    dp.message.register(get_audio, F.text == 'Получить аудио')

    dp.message.register(get_photo, Command(commands=['get_photo']))
    dp.message.register(get_photo, F.text == 'Получить фото')

    dp.message.register(get_git, Command(commands=['get_git']))
    dp.message.register(get_git, F.text == 'Получить ссылку на github')

    dp.message.register(stop, Command(commands=['stop']))
    dp.message.register(stop, F.text == 'Стоп')

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == '__main__':
    asyncio.run(start())
