from aiogram.filters import CommandStart, Command
from aiogram import Router, types, F
from keyboards import reply


user_router = Router()


@user_router.message(CommandStart())
async def start(message: types.Message):
    await message.answer("Этот бот разработан для заказов еды.", reply_markup=reply.start_kb)


@user_router.message(F.text.lower() == "меню")
@user_router.message(Command("menu"))
async def menu(message: types.Message):
    await message.answer("Вот наше меню:", reply_markup=reply.menu_kb)


@user_router.message(F.text.lower() == 'о нас')
@user_router.message(Command("about"))
async def about(message: types.Message):
    await message.answer("О нас: ")


@user_router.message(F.text.lower() == "контакты")
@user_router.message(Command("contacts"))
async def contacts(message: types.Message):
    await message.answer("Наши контакты: ", reply_markup=reply.contact_kb)


@user_router.message(F.text.lower() == "адреса")
@user_router.message(Command("addresses"))
async def addresses(message: types.Message):
    await message.answer("Наши адреса: ", reply_markup=reply.adres_kb)


@user_router.message(F.text.lower() == "назад")
async def back_home(message: types.Message):
    await message.answer("Главное меню", reply_markup=reply.start_kb)



# @user_router.message(F.text)
# @user_router.message(F.photo)
# @user_router.message(F.text.lower() == "доставка")
# @user_router.message(F.text.lower().contains("доставк"))
# @user_router.message(F.text.lower().startswith("как"))
# @user_router.message(F.text.lower().endswith("?"))
# @user_router.message((F.text.lower().contains("цен")) | (F.text.lower().contains("стоймост")))
async def echo(message: types.Message):
    await message.answer("Сработал магический фильтр")
