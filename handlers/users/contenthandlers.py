from aiogram import types
from aiogram.dispatcher import filters
from loader import dp


@dp.message_handler(content_types='document')
@dp.message_handler(content_types=types.ContentType.PHOTO)
async def photo_handler(msg:types.Message):
    await msg.answer("bu qanaqa rasm aka")

@dp.message_handler(content_types=types.ContentType.STICKER)
async def photo_handler(msg:types.Message):
    await msg.answer("hiring hirin :)")

@dp.message_handler(content_types=types.ContentType.CONTACT)
async def photo_handler(msg:types.Message):
    await msg.answer("kim bu shatalang")
    
@dp.message_handler(content_types=types.ContentType.VOICE)
async def photo_handler(msg:types.Message):
    await msg.answer("Yaxshi eshitmadim")


