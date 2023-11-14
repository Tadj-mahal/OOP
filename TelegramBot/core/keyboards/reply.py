from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, KeyboardButtonPollType

reply_keyboard = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text='Получить аудио'
        ),
        KeyboardButton(
            text='Получить фото'
        ),
    ],
    [
        KeyboardButton(
            text='Получить ссылку на github'
        ),
    ],
    [
        KeyboardButton(
            text='Стоп'
        ),
    ],
], resize_keyboard=True, one_time_keyboard=True, input_field_placeholder='Choose button.')