from data.loader import bot, dp, db
from aiogram.types import Message
from .text_handlers import start_register, show_main_menu


@dp.message_handler(commands=['start'])
async def command_start(message: Message):
    await message.answer('Добро пожаловать в бот доставки пиццы')
    user = db.get_user_by_id(message.chat.id)
    if user:
        '''Показать главное меню'''
        await show_main_menu(message)
    else:
        await start_register(message)
    # Регистрация по номеру телефона

@dp.message_handler(commands=['menu'])
async def command_menu(message: Message):
    await message.answer('https://telegra.ph/Nashe-Menyu-06-03-6')


@dp.message_handler(commands=['feedback'])
async def command_feedback(message: Message):
    await message.answer('<b>Единый call-center:</b> 1234 или +998 (71) 123-45-67')
