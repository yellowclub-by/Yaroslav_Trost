from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Меню"),
            KeyboardButton(text="О нас")
        ],

        [
            KeyboardButton(text="Контакты"),
            KeyboardButton(text="Адреса")
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder="Привет"

)

menu_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="С говядиной"),
            KeyboardButton(text="С курицой")
        ],

        [
            KeyboardButton(text="С колбасой"),
            KeyboardButton(text="Вегетарианскай")
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder="Привет"
)

contact_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Владелец = +375291111111"),
            KeyboardButton(text="Админ = +375292222222")
        ],

        [
            KeyboardButton(text="Работник = +375293333333"),
            KeyboardButton(text="Курьер = +375294444444")
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder="Привет"
)

adres_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Первый домик"),
            KeyboardButton(text="Второй домик")
        ],

        [
            KeyboardButton(text="Третий домик"),
            KeyboardButton(text="Четвертый денег")
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder="Привет"
)