from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from app.database.requests import get_genres, get_genre_arts

main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Каталог')],
                                     [KeyboardButton(text='Корзина')],
                                     [KeyboardButton(text='О нас')]],
                           resize_keyboard=True,
                           input_field_placeholder='Выберите пункт меню')

get_number = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Отправить номер', request_contact=True)]],
                                 resize_keyboard=True)

async def genres():
    all_genres = await get_genres()
    keyboard = InlineKeyboardBuilder()
    for genre in all_genres:
        keyboard.add(InlineKeyboardButton(text=genre.name, callback_data=f"genre_{genre.id}"))
    keyboard.add(InlineKeyboardButton(text='На главную', callback_data='to_main'))
    return keyboard.adjust(2).as_markup()

async def arts(genre_id):
    all_arts = await get_genre_arts(genre_id)
    keyboard = InlineKeyboardBuilder()
    for art in all_arts:
        keyboard.add(InlineKeyboardButton(text=art.name, callback_data=f"art_{art.id}"))
    keyboard.add(InlineKeyboardButton(text='На главную', callback_data='to_main'))
    return keyboard.adjust(2).as_markup()

def art_actions(art_id):
    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(text='Добавить в корзину', callback_data=f'add_cart_{art_id}'))
    keyboard.add(InlineKeyboardButton(text='На главную', callback_data='to_main'))
    return keyboard.adjust(1).as_markup()
