from aiogram.filters import CommandStart, Command
from aiogram import Router, types

user_router = Router()


@user_router.message(CommandStart())
async def start(message: types.Message):
    await message.answer("Этот бот разработан для заказов еды.")


@user_router.message(Command("menu"))
async def menu(message: types.Message):
    await message.answer("Вот наше меню:")


@user_router.message(Command("about"))
async def about(message: types.Message):
    await message.answer("О нас: ")


@user_router.message(Command("contacts"))
async def contacts(message: types.Message):
    await message.answer("Наши контакты: ")


@user_router.message(Command("addresses"))
async def addresses(message: types.Message):
    await message.answer("Наши адреса: ")


@user_router.message()
async def echo(message: types.Message):
    await message.answer("Бот находится в разработке(")
    user_text = message.text
    await message.answer(user_text)
