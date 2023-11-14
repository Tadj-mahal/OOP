from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from core.keyboards.reply import reply_keyboard

async def get_start(message: Message, bot: Bot):
    await message.answer(f'<tg-spoiler>Hello mir, manera krutit mir, v double cupe {message.from_user.first_name} !</tg-spoiler>')

async def get_hello(message: Message, bot: Bot):
    await message.answer(f'Привет! Ты можешь получить всю необходимую информацию по команде /info .')

async def get_info(message: Message, bot: Bot):
    await message.answer(f'Нажми на кнопку для получения необходимой информации.', reply_markup=reply_keyboard)

async def get_git(message: Message, bot: Bot):
    await message.answer(f'<tg-spoiler>https://github.com/Tadj-mahal/</tg-spoiler>', reply_markup=reply_keyboard)

async def stop(message: types.Message, bot: Bot):
    await message.reply("Бот останавливается...")
    # Останавливаем бота (можно здесь выполнить необходимые действия перед остановкой)
    await bot.close()