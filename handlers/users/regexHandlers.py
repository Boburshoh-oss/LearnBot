from aiogram import types
from aiogram.dispatcher import filters
from loader import dp

PHONE_NUMBER = r'^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$'
EMAIL_REGEX = r'[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+'
COMMAND_EMAIL_REGEX = r'/email:' + EMAIL_REGEX

@dp.message_handler(filters.Regexp(EMAIL_REGEX))
async def regexp_email(msg:types.Message):
    await msg.answer("Email qabul qilindi")

@dp.message_handler(filters.Regexp(PHONE_NUMBER))
async def regexp_phone(msg:types.Message):
    await msg.answer("Telfon raqam qabul qilindi")
    
@dp.message_handler(regexp_commands=[COMMAND_EMAIL_REGEX])
async def regexp_command_email(msg:types.Message):
    await msg.answer("email bilan qabul qildin")