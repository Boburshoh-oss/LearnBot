from aiogram import types
from aiogram.dispatcher import filters
from loader import dp

@dp.message_handler(filters.Text(contains='assalom', ignore_case=True))
@dp.message_handler(filters.Text(equals='assalom alaykum',ignore_case=True))
async def text_example(msg:types.Message):
    await msg.reply("Va alaykum assalom botam") 

@dp.message_handler(filters.Text(contains='ahmoq',ignore_case=True))
async def text_example(msg:types.Message):
    await msg.reply("O'zing ahmoq maymun") 