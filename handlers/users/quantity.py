from aiogram import Router, types, F
from states.store import StoreStates
from aiogram.fsm.context import FSMContext
from keyboards.reply.main import get_cats_markup
from loader import db

router = Router()


@router.message(StoreStates.quantity, F.text.in_([str(i) for i in range(1, 10)]))
async def get_quantity(message: types.Message, state: FSMContext):
    quantity = message.text
    cats = await db.select_all_cats()
    data = await state.get_data()
    product_id = data.get("product_id")
    markup = get_cats_markup(cats)
    # Mahsulotni savatga qo'shish
    user = await db.select_user(telegram_id=message.from_user.id)
    if user:
        cart = await db.select_cart(user_id=user["id"])
        if cart and product_id:
            product = await db.select_cart_item(cart_id=cart["id"], product_id=product_id)
            if product is None:
                await db.add_cart_items(cart_id=cart["id"], product_id=product_id, quantity=int(quantity))
            else:
                await db.update_cart_item_quantity(new_quantity=int(quantity) + product["quantity"], cart_id=cart["id"], product_id=product_id)
    # Qo'shilganligi haqida xabar yuborish
    await message.answer(f"✅ {quantity} ta mahsulot savatga qo'shildi!")
    await message.answer("Yana nima buyurtma qilishni hohlaysiz 🙂", reply_markup=markup)
    await state.set_state(StoreStates.category)
