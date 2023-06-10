from data.loader import dp, bot, db
from aiogram.types import Message
from states.states import NumberState
from aiogram.dispatcher import FSMContext
import re
from data.configs import CODE
from random import choice
from keyboards.reply import generate_main_menu, generate_delivery_type, \
    generate_choice_filials, generate_choice_settings


async def start_register(message: Message, state=None):
    await NumberState.phone.set()
    await message.answer('Отправьте свой номер телефона в формате: +998 ** *** ** **')


@dp.message_handler(state=NumberState.phone)
async def get_phone(message: Message, state: FSMContext):
    phone = message.text
    result1 = re.search(r'\+998 \d\d \d\d\d \d\d \d\d$', phone)
    result2 = re.search(r'\+998\d{9}$', phone)
    if result1 or result2:
        await message.answer('Ok')
        text = ''
        answer = ''
        for i in range(4):
            random_num = choice(list(CODE.keys()))
            text += random_num + ' '
            answer += CODE[random_num]

        async with state.proxy() as data:
            data['phone'] = phone
            data['answer'] = answer

        await NumberState.next()
        await message.answer(f'Вам отправили код. Введите код в формате 1234:\n{text}')
    else:
        await message.answer('No')
        await state.finish()
        await again_ask_phone(message)


async def again_ask_phone(message:Message, state=None):
    await NumberState.phone.set()
    await message.answer('''Не верный формат номера или номер.
Отправьте свой номер телефона в формате: +998 ** *** ** **''')

@dp.message_handler(state=NumberState.code)
async def get_code(message: Message, state: FSMContext):
    code = message.text
    async with state.proxy() as data:
        answer = data['answer']
        phone = data['phone']
        if code == answer:
            await message.answer('Код совпал')
            chat_id = message.chat.id
            full_name = message.from_user.full_name
            db.insert_user(chat_id, full_name, phone)
            await state.finish()
            await show_main_menu(message)
        else:
            await message.answer('Код не совпал')
            # Написать функцию, которая просит код заново
            await state.finish()
            await start_register(message)

@dp.message_handler(regexp='🏠 Главное меню')
async def show_main_menu(message: Message):
    await message.answer('Выберите раздел: ', reply_markup=generate_main_menu())


@dp.message_handler(regexp='🍴 Меню')
@dp.message_handler(regexp='🚗 К выбору доставки')
async def show_choice_delivery(message: Message):
    await message.answer('Выберите тип доставки',
                         reply_markup=generate_delivery_type())


@dp.message_handler(regexp='🏃‍♀️Самовывоз')
async def show_choice_filials(message: Message):
    await message.answer('Выберите филиал: ',
                         reply_markup=generate_choice_filials())


@dp.message_handler(regexp='🚀 О доставке')
async def return_delivery_msg(ctx: Message):
    await ctx.answer('Если не успеем доставить заказ в течении 60 минут, мы отправим Вам подарок промокод на большую пиццу.\n\nДоставка бесплатная. Сумма заказа от 45.000 сум.')

@dp.message_handler(regexp='⚙️ Настройки')
async def show_choice_settings(ctx: Message):
    await ctx.answer('⚙️ Настройки', reply_markup=generate_choice_settings())


filial = [i[0] for i in db.get_filials()]

@dp.message_handler(lambda message: message.text in filial)
async def show_menu(message: Message):
    pass


