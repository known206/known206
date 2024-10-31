from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Botni ishga tushurish"),
            types.BotCommand("help", "Yordam"),
            types.BotCommand("ban","Foydalanuvchini banlash"),
            types.BotCommand("unban","Foydalanuvchini bandan chiqarish"),
            types.BotCommand("set_photo","Guruh rasmini o'zgartirish"),
            types.BotCommand("ro","Foydalanuvchini yozishdan cheklash"),
            types.BotCommand("unro","Foydalanuvchini yozish holatiga qaytarish"),
            types.BotCommand("mute_all","Barcha foydalanuvchilarni yozishni cheklash"),
            types.BotCommand("set_title","Guruh nomini almashtirish"),
            types.BotCommand("set_description","Guruh ma'lumotlarini almashtirish"),
        ]
    )
