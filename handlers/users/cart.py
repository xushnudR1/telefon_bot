from aiogram import Router, types, F
from states.store import StoreStates
from aiogram.fsm.context import FSMContext
from loader import db
from utils.misc.extra import get_cart_detail_text
from keyboards.inline.cart import get_cart_items_markup, get_cart_detail

router = Router()

@router.message(F.text == "📥 Savatcha")
async def cart_detail(message: types.Message, state: FSMContext):
    user = await db.select_user(telegram_id=message.from_user.id)
    if user:
        cart = await db.select_cart(user_id=user["id"])
        cart_items = await db.select_cart_items(cart_id=cart["id"])
        if cart_items:
            text = await get_cart_detail_text(cart_items=cart_items)
            markup = await get_cart_items_markup(cart_items=cart_items)
            await message.answer(text=text, reply_markup=markup)
        else:
            await message.answer("Sizning savatcha hozircha bo'sh, buni to'g'irlaymizmi?")


@router.callback_query(F.data == "back_cart")
async def go_cart_detail(call: types.CallbackQuery):
    user = await db.select_user(telegram_id=call.from_user.id)
    if user:
        cart = await db.select_cart(user_id=user["id"])
        cart_items = await db.select_cart_items(cart_id=cart["id"])
        if cart_items:
            markup = await get_cart_items_markup(cart_items=cart_items)
            await call.message.edit_reply_markup(reply_markup=markup)


@router.callback_query(F.data.startswith('minus'))
async def update_cart_item_quantity(call: types.CallbackQuery):
    action, product_id = call.data.split("_")
    user = await db.select_user(telegram_id=call.from_user.id)
    if user:
        cart = await db.select_cart(user_id=user["id"])
        cart_item = await db.select_cart_item(cart_id=cart["id"], product_id=int(product_id))
        if cart_item["quantity"] - 1 == 0:
            await db.delete_cart_item(cart_item=cart_item["id"])
            cart_items = await db.select_cart_items(cart_id=cart["id"])
            if cart_items:
                text = await get_cart_detail_text(cart_items=cart_items)
                markup = await get_cart_items_markup(cart_items=cart_items)
                await call.message.edit_text(text=text, reply_markup=markup)
            else:
                await call.message.delete()
                await call.message.answer("Sizning savatcha hozircha bo'sh, buni to'g'irlaymizmi?") 
        else:
            await db.update_cart_item_quantity(new_quantity=cart_item["quantity"] - 1, cart_id=cart["id"], product_id=int(product_id))
            cart_items = await db.select_cart_items(cart_id=cart["id"])
            if cart_items:
                text = await get_cart_detail_text(cart_items=cart_items)
                markup = get_cart_detail(product_id=int(product_id), quantity=cart_item["quantity"] - 1)
                await call.message.edit_text(text=text, reply_markup=markup)


@router.callback_query(F.data.startswith('plus'))
async def update_cart_item_quantity(call: types.CallbackQuery):
    action, product_id = call.data.split("_")
    user = await db.select_user(telegram_id=call.from_user.id)
    if user:
        cart = await db.select_cart(user_id=user["id"])
        cart_item = await db.select_cart_item(cart_id=cart["id"], product_id=int(product_id))
        await db.update_cart_item_quantity(new_quantity=cart_item["quantity"] + 1, cart_id=cart["id"], product_id=int(product_id))
        cart_items = await db.select_cart_items(cart_id=cart["id"])
        if cart_items:
            text = await get_cart_detail_text(cart_items=cart_items)
            markup = get_cart_detail(product_id=int(product_id), quantity=cart_item["quantity"] + 1)
            await call.message.edit_text(text=text, reply_markup=markup)


@router.callback_query(F.data == "clear_cart")
async def user_clear_cart(call: types.CallbackQuery):
    user = await db.select_user(telegram_id=call.from_user.id)
    if user:
        cart = await db.select_cart(user_id=user["id"])
        await db.clear_cart(cart_id=cart["id"])
        await call.message.delete()
        await call.message.answer("Savatingizdagi mahsulotlar o'chirildi!")


@router.callback_query(F.data)
async def cart_product_detail(call: types.CallbackQuery, state: FSMContext):
    cart_item = await db.select_cart_item(id=int(call.data))
    print(cart_item)
    await call.message.edit_reply_markup(reply_markup=get_cart_detail(product_id=cart_item['product_id'], quantity=cart_item['quantity']))