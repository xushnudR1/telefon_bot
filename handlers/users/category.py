from aiogram import Router, types, F
from states.store import StoreStates
from keyboards.reply.main import get_cats_markup
from aiogram.fsm.context import FSMContext
from loader import db

router = Router()


@router.message(StoreStates.category, F.text)
async def all_cats(message: types.Message, state: FSMContext):
    category = await db.select_category(name=message.text)
    if category:
        await state.set_data({"parent_id": category["parent_id"]})
        sub_cats = await db.select_cats_by_parent_id(parent_id=category["id"])
        if sub_cats:
            await message.answer(f"Siz {category['name']} bo'limini tanladingiz", reply_markup=get_cats_markup(cats=sub_cats, back=True))
        else:
            products = await db.select_product_by_category(category_id=category["id"])
            await message.answer(f"Siz {category['name']} bo'limini tanladingiz", reply_markup=get_cats_markup(cats=products, back=True))
            await state.set_state(StoreStates.product)
    else:
        await message.answer(f"Iltimos, quyidagi bo'limlardan birini tanlang 🔽")