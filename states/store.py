from aiogram.filters.state import StatesGroup, State


class StoreStates(StatesGroup):
    category = State()
    product = State()
    quantity = State()
    confirm = State()
