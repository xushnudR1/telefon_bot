from aiogram import Router, types
from aiogram.filters import CommandStart
from aiogram.client.session.middlewares.request_logging import logger
from keyboards.reply.main import get_cats_markup
from states.store import StoreStates
from aiogram.fsm.context import FSMContext
from loader import db

router = Router()


@router.message(CommandStart())
async def do_start(message: types.Message, state: FSMContext):
    telegram_id = message.from_user.id
    full_name = message.from_user.full_name
    username = message.from_user.username
    try:
        await db.add_user(telegram_id=telegram_id, full_name=full_name, username=username)
    except Exception as error:
        logger.info(error)
    user = await db.select_user(telegram_id=telegram_id)
    if user:
        cart = await db.select_cart(user_id=user["id"])
        if cart is None:
            await db.add_cart(user_id=user["id"])
    cats = await db.select_all_cats()
    markup = get_cats_markup(cats)
    await message.answer(f"Assalomu alaykum {full_name}!", reply_markup=markup)
    await state.set_state(StoreStates.category)