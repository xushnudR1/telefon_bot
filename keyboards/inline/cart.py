from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from loader import db

async def get_cart_items_markup(cart_items):
    inline_keyboards = []
    for cart_item in cart_items:
        product = await db.select_product(id=cart_item["product_id"])
        name = InlineKeyboardButton(text=f"{product['name']}", callback_data=f"{cart_item['id']}")
        inline_keyboards.append([name])
    inline_keyboards.append([InlineKeyboardButton(text="🗑 Savatni tozalash", callback_data="clear_cart")])
    markup = InlineKeyboardMarkup(inline_keyboard=inline_keyboards)
    return markup

def get_cart_detail(product_id, quantity):
    minus = InlineKeyboardButton(text="➖", callback_data=f"minus_{product_id}")
    plus = InlineKeyboardButton(text="➕", callback_data=f"plus_{product_id}")
    count = InlineKeyboardButton(text=f"{quantity}", callback_data=f"{quantity}")
    back = InlineKeyboardButton(text="⬅️ Orqaga", callback_data=f"back_cart")
    markup = InlineKeyboardMarkup(inline_keyboard=[[minus, count, plus], [back]])
    return markup
