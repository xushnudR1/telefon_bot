from aiogram import Router

from filters import ChatPrivateFilter


def setup_routers() -> Router:
    from .users import start, back, category, product, quantity, cart, confirm
    from .errors import error_handler
    
    router = Router()
    
    # Устанавливаем локальный фильтр, если нужно
    start.router.message.filter(ChatPrivateFilter(chat_type=["private"]))
    
    router.include_routers(start.router, cart.router, confirm.router, back.router, category.router, product.router, quantity.router, error_handler.router)
    
    return router
