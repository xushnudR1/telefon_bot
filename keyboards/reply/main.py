from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def get_cats_markup(cats, back=False) -> ReplyKeyboardMarkup:
    keyboards = []
    rows = []
    for cat in cats:
        rows.append(KeyboardButton(text=cat["name"]))
    length = len(rows)
    for index in range(1, length + 1, 2):
        try:
            keyboards.append(rows[index - 1:index + 1])
        except IndexError:
            keyboards.append(rows[index - 1:])
    keyboards.append([KeyboardButton(text="📥 Savatcha"), KeyboardButton(text="🛒 Rasmiylashtirish")])
    if back:
        keyboards.append([KeyboardButton(text="⬅️ Orqaga")])
    kb = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=keyboards)
    return kb


def get_numbers(number=9):
    kb = ReplyKeyboardBuilder()
    for i in range(1, number + 1):
        kb.add(KeyboardButton(text=str(i)))
    kb.add(KeyboardButton(text="🏠 Bosh menyu"), KeyboardButton(text="⬅️ Orqaga"))
    kb.adjust(3)
    return kb.as_markup(reply_markup=True)


def phone_markup():
    kb = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[[
        KeyboardButton(text="📱 Telefon raqamni tasdiqlash", request_contact=True)
    ], [
        KeyboardButton(text="⬅️ Orqaga")
    ]])
    return kb


def get_location():
    kb = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[[
        KeyboardButton(text="📍 Joylashuvni ulashish", request_location=True)
    ], [
        KeyboardButton(text="⬅️ Orqaga")
    ]])
    return kb
