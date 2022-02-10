from aiogram import types
from aiogram.dispatcher import filters
from loader import dp

@dp.message_handler(hashtags='money')
@dp.message_handler(cashtags=['eur','usd'])
async def hashtag_example(msg:types.Message):
    await msg.answer("Yeee, akang kuchaydi")