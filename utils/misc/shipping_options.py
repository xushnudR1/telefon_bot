from aiogram import types
from aiogram.types import LabeledPrice

REGULAR_SHIPPING = types.ShippingOption(
    id='post_reg',
    title="Fargo (3 kun)",
    prices=[
        LabeledPrice(label='Maxsus quti', amount=1500000),
        LabeledPrice(label='3 ish kunida yetkazish', amount=5000000),
    ]
)

FAST_SHIPPING = types.ShippingOption(
    id='post_fast',
    title='Express pochta (1 kun)',
    prices=[
        LabeledPrice(
            label='1 kunda yetkazish', amount=9000000),
    ]
)

PICKUP_SHIPPING = types.ShippingOption(id='pickup', title="Do'kondan olib ketish", prices=[LabeledPrice(label="Yetkazib berishsiz", amount=0)])