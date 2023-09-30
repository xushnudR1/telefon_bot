# 13 599 000
from loader import db

def format_price(price):
    float_price = str(price)[-1:]
    price = str(int(price))[::-1]
    s = ""
    index = 0
    for _ in range(len(price) // 3 + 1):
        try:
            s += price[index:index+3] + " "
        except IndexError:
            s += price[index:]
        index += 3
    return s[::-1].strip() + f".{float_price}"

async def get_cart_detail_text(cart_items):
    total_price = 0
    message = f"<b>Siz buyurtma qilgan mahsulotlar</b>\n\n"
    for cart_item in cart_items:
        product = await db.select_product(id=cart_item["product_id"])
        price = product["price"] * cart_item["quantity"]
        message += f"<i>{product['name']} x {cart_item['quantity']} = {format_price(float(price))} so'm</i>\n"
        total_price += price
    message += f"\n<b>Umumiy: {format_price(float(total_price))} so'm</b>"
    return message


async def get_total_price(cart_items):
    total_price = 0
    for cart_item in cart_items:
        product = await db.select_product(id=cart_item["product_id"])
        price = product["price"] * cart_item["quantity"]
        total_price += price

    return total_price
