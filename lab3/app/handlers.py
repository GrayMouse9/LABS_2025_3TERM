from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

import app.keyboards as kb
import app.database.requests as rq

router = Router()

class Register(StatesGroup):
    name = State()
    age = State()
    number = State()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await rq.set_user(message.from_user.id)
    await rq.clear_cart(message.from_user.id)
    await message.answer('Добро пожаловать в галерею искусств!', reply_markup=kb.main)

@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer("Это команда /help. Чем я могу помочь?")

@router.message(F.text == 'Каталог')
async def catalog(message: Message):
    await message.answer("Выберите жанр произведения", reply_markup=await kb.genres())

@router.callback_query(F.data.startswith('genre_'))
async def genre_selected(callback: CallbackQuery):
    genre_id = callback.data.split('_')[1]
    await callback.answer('Вы выбрали жанр')
    await callback.message.edit_text('Выберите произведение',
                                     reply_markup=await kb.arts(genre_id))

@router.callback_query(F.data.startswith('art_'))
async def art_selected(callback: CallbackQuery):
    art_id = callback.data.split('_')[1]
    art_data = await rq.get_art(art_id)
    await callback.answer('Вы выбрали картину')

    await callback.message.edit_text(
        f'Название: "{art_data.name}"\n'
        f'Художник: {art_data.artist}\n'
        f'Цена: {art_data.price} $',
        reply_markup=kb.art_actions(art_id)
          )

@router.message(Command('register'))
async def register(message: Message, state: FSMContext):
    await state.set_state(Register.name)
    await message.answer('Введите ваше имя')

@router.message(Register.name)
async def register_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Register.age)
    await message.answer('Введите ваш возраст')

@router.message(Register.age)
async def register_age(message: Message, state: FSMContext):
    await state.update_data(age=message.text)
    await state.set_state(Register.number)
    await message.answer('Отправьте ваш номер телефона', reply_markup=kb.get_number)

@router.callback_query(F.data.startswith('art_'))
async def art_selected(callback: CallbackQuery):
    art_id = callback.data.split('_')[1]
    art_data = await rq.get_art(art_id)

    await callback.message.edit_text(
        f'Название: "{art_data.name}"\n'
        f'Художник: {art_data.artist}\n'
        f'Цена: {art_data.price} $',
        reply_markup=kb.art_actions(art_id) # <--- Прикрепляем новую клавиатуру
    )

@router.callback_query(F.data.startswith('add_cart_'))
async def add_to_cart_handler(callback: CallbackQuery):
    art_id = callback.data.split('_')[2]
    await rq.add_to_cart(callback.from_user.id, art_id)

    await callback.answer('Товар добавлен в корзину!')

@router.message(F.text == 'Корзина')
async def show_cart(message: Message):

    cart_items = await rq.get_cart(message.from_user.id)


    items_list = list(cart_items)
    if not items_list:
        await message.answer("Ваша корзина пуста 🗑")
        return

    await message.answer("🛒 <b>Ваша корзина:</b>", parse_mode='HTML')

    total_price = 0
    for item in items_list:
        await message.answer(f'🖼 <b>{item.name}</b>\nАвтор: {item.artist}\nЦена: {item.price} $', parse_mode='HTML')
        total_price += item.price

    await message.answer(f'💰 <b>Итого: {total_price} $</b>', parse_mode='HTML')

@router.message(F.text == 'О нас')
async def about_us(message: Message):
    about_text = (
        "👋 Добро пожаловать в Арт-галерею!\n\n"
        "Я — Арт-Бот, ваш персональный проводник в мире искусства.\n\n"
        "Моя задача — помочь вам легко найти, просмотреть и выбрать произведение, "
        "которое вам понравится.\n\n"
        "Надеюсь, вам будет комфортно и интересно в моей галерее! 🖼️"
    )
    await message.answer(about_text)
