from aiogram import Router, types, F
from states.store import StoreStates
from utils.misc.extra import format_price
from aiogram.fsm.context import FSMContext
from keyboards.reply.main import get_numbers
from loader import db

router = Router()


@router.message(StoreStates.product, F.text)
async def get_product_detail(message: types.Message, state: FSMContext):
    product = await db.select_product(name=message.text)
    if product:
        await state.update_data({"category_id": product["category_id"], "product_id": product["id"]})
        caption = f"<b>{product['name']}</b>\n\n{product['description']}\n\n<b>Narx: {format_price(float(product['price']))} mln so'm</b>"
        await message.answer_photo(photo=product["image_url"], caption=caption, reply_markup=get_numbers())
        await state.set_state(StoreStates.quantity)
    else:
        await message.answer("Bunday mahsulot mavjud emas! Tugmalardan birini tanlang 🔽")