from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from data.loader import db

def generate_main_menu():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    menu = KeyboardButton(text='🍴 Меню')
    contacts = KeyboardButton(text='☎ Контакты')
    review = KeyboardButton(text='✍ Оставить отзыв')
    delivery = KeyboardButton(text='🚀 О доставке')
    settings = KeyboardButton(text='⚙ Настройки')
    markup.row(menu)
    markup.row(contacts, review)
    markup.row(delivery, settings)
    return markup


def generate_delivery_type():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    delivery = KeyboardButton(text='🚗 Доставка')
    self_delivery = KeyboardButton(text='🏃‍♀️Самовывоз')
    back_btn = KeyboardButton(text='🏠 Главное меню')
    markup.row(delivery, self_delivery)
    markup.row(back_btn)
    return markup


def generate_choice_filials():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    back_btn = KeyboardButton(text='🚗 К выбору доставки')
    buttons = []
    filials = db.get_filials()  # [(Максимка), (Чорсу)]
    for filial in filials:
        btn = KeyboardButton(text=filial[0]) # (Максимка) -> максимка
        buttons.append(btn)
    markup.add(back_btn)
    markup.add(*buttons)
    return markup


def generate_choice_settings():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    language = KeyboardButton(text='🌐 Выбрать язык')
    number = KeyboardButton(text='📱 Сменить номер')
    back_btn = KeyboardButton(text='🏠 Главное меню')
    markup.add(language)
    markup.add(number)
    markup.add(back_btn)
    return markup
