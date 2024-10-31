import io
from aiogram.dispatcher.filters import Command
from aiogram import types
from loader import dp,bot
from filters import IsGroup
from filters.admins import AdminFilter


#guruh rasmini almashtirish
@dp.message_handler(IsGroup(),AdminFilter(),Command('set_photo',prefixes='*^'))
async def set_photo(message:types.Message):
    try:
        source_message=message.reply_to_message
        if source_message and source_message.photo:
            photo=source_message.photo[-1]
            photo=await photo.download(destination=io.BytesIO())
            input_file=types.InputFile(photo)

            #guruh rasmini o'zgartirish
            await message.chat.set_photo(photo=input_file)
            await message.reply("Guruh rasmi Muvaffaqiyatli almashtirildi.")
        else:
            await message.reply("Iltimos yangi rasmni reply qiling.")
    except:
        await message.reply("Xatolik!")

#guruh nomini almashtirish title()

@dp.message_handler(IsGroup(),AdminFilter(),Command('set_title',prefixes='*^'))
async def set_group_title(message:types.Message):
    source_message=message.reply_to_message
    if source_message and source_message.text:
        title=source_message.text
        await bot.set_chat_title(message.chat.id,title=title)
        await message.reply("Guruh nomi muvaffaqiyatli almashtirildi.")
    else:
        await message.reply("Iltimos yangi guruh nomini qaytadan reply qiling.")

#guruh desc almashtirish
@dp.message_handler(IsGroup(),AdminFilter(),Command('set_description',prefixes='*^'))
async def set_group_descrp(message:types.Message):
    source_message=message.reply_to_message
    if source_message and source_message.text:
        description=source_message.text
        await message.chat.set_description(description)
        await message.reply("Guruh ma'lumotlari muvaffaqiyatli almashtirildi.")

    else:
        await message.reply("Xatolik! Qaytadan urinib ko'ring.")











