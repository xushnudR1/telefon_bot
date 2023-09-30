from aiogram import Bot
from data.config import BOT_TOKEN
from aiogram.enums import ParseMode
from utils.db.postgres import Database

db = Database()
bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)