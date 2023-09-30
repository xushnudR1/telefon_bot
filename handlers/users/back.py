from aiogram import Router, types, F
from states.store import StoreStates
from keyboards.reply.main import get_cats_markup
from aiogram.fsm.context import FSMContext
from loader import db

router = Router()


@router.message(StoreStates.product, F.text == "⬅️ Orqaga")
@router.message(StoreStates.category, F.text == "⬅️ Orqaga")
async def back_previous_state(message: types.Message, state: FSMContext):
    data = await state.get_data()
    parent_id = data.get("parent_id")
    if parent_id:
        category = await db.select_category(id=parent_id)
        await state.update_data({"parent_id": category["parent_id"]})
        cats = await db.select_cats_by_parent_id(parent_id=parent_id)
        await message.answer(f"Oldingi bo'limga qaytdingiz", reply_markup=get_cats_markup(cats=cats, back=True))
        await state.set_state(StoreStates.category)
    else:
        cats = await db.select_all_cats()
        await message.answer(f"Asosiy bo'limga qaytdingiz", reply_markup=get_cats_markup(cats=cats))


@router.message(StoreStates.quantity, F.text == "⬅️ Orqaga")
async def back_product_state(message: types.Message, state: FSMContext):
    data = await state.get_data()
    category_id = data.get("category_id")
    products = await db.select_product_by_category(category_id=category_id)
    await message.answer(f"Oldingi bo'limga qaytdingiz", reply_markup=get_cats_markup(cats=products, back=True))
    await state.set_state(StoreStates.product)


@router.message(StoreStates.quantity, F.text == "🏠 Bosh menyu")
async def back_main_menu(message: types.Message, state: FSMContext):
    cats = await db.select_all_cats()
    markup = get_cats_markup(cats)
    await message.answer("Bosh menyudasiz", reply_markup=markup)
    await state.set_state(StoreStates.category)
