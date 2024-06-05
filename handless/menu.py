from aiogram import Router, types, F
from aiogram.types import FSInputFile
menu_router = Router()


@menu_router.message(F.text.lower() == "с говядиной")
async def messa(message: types.Message):
    photo = FSInputFile("img\menu\шаурмаговядина.jpg")
    await message.answer_photo(photo, caption="Шаурма с говядиной")

@menu_router.message(F.text.lower() == "с курицой")
async def messa(message: types.Message):
    photo = FSInputFile("img\menu\шаурма.jpg")
    await message.answer_photo(photo, caption="Шаурма с курицей")

@menu_router.message(F.text.lower() == "с колбасой")
async def messa(message: types.Message):
        photo = FSInputFile("img\menu\шармаколбаса.jpg")
        await message.answer_photo(photo, caption="Шаурма с колбасой")

@menu_router.message(F.text.lower() == "вегетарианскай")
async def messa(message: types.Message):
        photo = FSInputFile("img\menu\шаурмавег.jpg")
        await message.answer_photo(photo, caption="Шаурма вегетарианская")