from aiogram import Router, types, F
from states.store import StoreStates
from aiogram.fsm.context import FSMContext
from loader import db, bot
from utils.misc.extra import get_cart_detail_text, get_total_price
from keyboards.reply.main import phone_markup, get_location
from keyboards.reply.main import get_cats_markup
from utils.misc.invoice import Invoice
from utils.misc.shipping_options import REGULAR_SHIPPING, FAST_SHIPPING, PICKUP_SHIPPING
from data.config import ADMINS

router = Router()

@router.message(F.text == "🛒 Rasmiylashtirish")
async def confirm_order(message: types.Message, state: FSMContext):
    user = await db.select_user(telegram_id=message.from_user.id)
    if user:
        cart = await db.select_cart(user_id=user["id"])
        cart_items = await db.select_cart_items(cart_id=cart["id"])
        if cart_items:
            text = await get_cart_detail_text(cart_items=cart_items)
            await message.answer(text)
            await message.answer("Buyurtmani tasdiqlash uchun telefon raqamingizni jo'nating", reply_markup=phone_markup())
            await state.set_state(StoreStates.confirm)


@router.message(StoreStates.confirm, F.contact)
async def get_phone_number(message: types.Message, state: FSMContext):
    phone_number = message.contact.phone_number
    await state.update_data({"phone_number": phone_number})
    await message.answer("Raqamingiz saqlandi, endi joriy joylashuvni jo'nating", reply_markup=get_location())


@router.message(StoreStates.confirm, F.location)
async def get_live_location(message: types.Message, state: FSMContext):
    lat = message.location.latitude
    lon = message.location.longitude
    data = await state.get_data()
    phone_number = data.get("phone_number")
    cats = await db.select_all_cats()
    markup = get_cats_markup(cats)
    # save order
    user = await db.select_user(telegram_id=message.from_user.id)
    cart = await db.select_cart(user_id=user["id"])
    cart_items = await db.select_cart_items(cart_id=cart["id"])
    total_price = await get_total_price(cart_items=cart_items)
    await db.add_order(user_id=user["id"], paid=False, total_price=total_price, lat=lat, lon=lon, phone_number=phone_number)

    prices = []
    # get_last_order
    order = await db.select_order(user_id=user["id"], paid=False, total_price=total_price)
    for cart_item in cart_items:
        product = await db.select_product(id=cart_item["product_id"])
        prices.append(
            types.LabeledPrice(
                label=f"{product['name']} x {cart_item['quantity']}",
                amount=int(cart_item['quantity'] * product['price'] * 100)
            )
        )
        await db.add_order_item(order_id=order["id"], product_id=cart_item["product_id"], quantity=cart_item["quantity"], price=product["price"])
        await db.clear_cart(cart_id=cart["id"])

    # create Invoice
    invoice = Invoice(
        title=f"{order['id']}-buyurtma uchun to'lov qiling",
        description="Siz buyurtma qilgan mahsulotlar ro'yhati bilan tanishing!",
        currency="UZS",
        prices=prices,
        start_parameter=f"create_invoice_order_{order['id']}",
        need_email=True,
        need_name=True,
        need_phone_number=True,
        need_shipping_address=True, # foydalanuvchi manzilini kiritishi shart
        is_flexible=True
    )

    await message.answer("✅ Barcha ma'lumotlar saqlandi, endi to'lov qilishingiz kerak!", reply_markup=markup)
    
    # send invoice
    await bot.send_invoice(chat_id=message.from_user.id, **invoice.generate_invoice(), payload=f"order:{order['id']}")

    await state.set_state(StoreStates.category)


@router.shipping_query(StoreStates.category)
async def choose_shipping(query: types.ShippingQuery):
    if query.shipping_address.country_code != "UZ":
        await bot.answer_shipping_query(shipping_query_id=query.id,
                                        ok=False,
                                        error_message="Chet elga yetkazib bera olmaymiz")
    elif query.shipping_address.city.lower() == "urganch":
        await bot.answer_shipping_query(shipping_query_id=query.id,
                                        shipping_options=[FAST_SHIPPING, REGULAR_SHIPPING, PICKUP_SHIPPING],
                                        ok=True)
    else:
        await bot.answer_shipping_query(shipping_query_id=query.id,
                                        shipping_options=[REGULAR_SHIPPING],
                                        ok=True)


@router.pre_checkout_query(StoreStates.category)
async def process_pre_checkout_query(pre_checkout_query: types.PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_query_id=pre_checkout_query.id,
                                        ok=True)
    await bot.send_message(chat_id=pre_checkout_query.from_user.id,
                           text="Xaridingiz uchun rahmat!\n\nSiz bilan tezda bog'lanamiz!")
    await bot.send_message(chat_id=ADMINS[0],
                           text=f"Quyidagi mahsulot sotildi: {pre_checkout_query.invoice_payload}\n"
                                f"ID: {pre_checkout_query.id}\n"
                                f"Telegram user: {pre_checkout_query.from_user.first_name}\n"
                                f"Xaridor: {pre_checkout_query.order_info.name}, tel: {pre_checkout_query.order_info.phone_number}")
    invoice_payload = pre_checkout_query.invoice_payload.split(":")
    order_id = invoice_payload[1]

    await db.update_order_paid_status(order_id=int(order_id), paid=True)
