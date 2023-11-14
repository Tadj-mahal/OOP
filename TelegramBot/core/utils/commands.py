from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault

async def set_commands(bot: Bot):
    commands = [
        BotCommand(
            command='start',
            description='Начало работы'
        ),
        BotCommand(
            command='info',
            description='Отобразить доступный функционал'
        ),
        BotCommand(
            command='get_photo',
            description='Получить фото'
        ),
        BotCommand(
            command='get_audio',
            description='Получить аудио'
        ),
        BotCommand(
            command='get_git',
            description='Получить git'
        ),
        BotCommand(
            command='stop',
            description='Остановить бота'
        )
    ]

    await bot.set_my_commands(commands, BotCommandScopeDefault())