from aiogram import types
from aiogram.dispatcher import filters
from loader import dp

SUPERUSERS = [542470747]
BAN_LIST = [1342805581]

@dp.message_handler(chat_id=SUPERUSERS, text='secret')
async def id_filter_example(msg:types.Message):
    await msg.answer("Xush kelibsiz SuperUsers")