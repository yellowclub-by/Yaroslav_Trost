import asyncio
from aiogram import Bot, Dispatcher



TOKEN = "7105685653:AAHwihb5Wq-Qwi0Lm4HBtH7Gvbl-ZsY2w7k"
bot = Bot(token=TOKEN)
dp = Dispatcher()

from handless.user_privat import user_router
from handless.user_group import group_router
dp.include_router(user_router)
dp.include_router(group_router)







async def main():
    print("Бот запущен")
    await dp.start_polling(bot)


asyncio.run(main())
