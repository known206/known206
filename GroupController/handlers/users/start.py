from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from filters import IsPrivate


from loader import dp


@dp.message_handler(IsPrivate(),commands='start')
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}! Bot yaratuvchisi @troubl_e")
