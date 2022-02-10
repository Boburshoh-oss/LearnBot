from aiogram import types
from aiogram.dispatcher.filters.builtin import Command
from aiogram.dispatcher.filters import AdminFilter
from loader import dp

@dp.message_handler(Command("change_photo"),AdminFilter())
@dp.message_handler(commands="change_photo",is_chat_admin=True)
async def chat_admin_example(msg:types.Message):
    await msg.answer("Rasm almashtiramizmi?")