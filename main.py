import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart

TOKEN = "7105685653:AAHwihb5Wq-Qwi0Lm4HBtH7Gvbl-ZsY2w7k"
bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: types.Message):
    await message.answer("Этот бот разработан для заказов еды.")


@dp.message()
async def echo(message: types.Message):
    await message.answer("Бот находится в разработке(")
    user_text = message.text
    await message.answer(user_text)


async def main():
    print("Бот запущен")
    await dp.start_polling(bot)


asyncio.run(main())
