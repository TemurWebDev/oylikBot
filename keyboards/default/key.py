from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from handlers.users.baza import sana

BoshMenu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🙎🏻‍♂️ My accaunt"),
            KeyboardButton(text="💰 Oylik"),

        ],
        [
            KeyboardButton(text="🗯️ Fikr bildirish")
        ]

    ],
    resize_keyboard=True
)


Oylik = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Mart"),
            KeyboardButton(text="Aprel"),

        ],

    ],
    resize_keyboard=True
)


tel = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Nomer yuborish",request_contact=True),

        ],

    ],
    resize_keyboard=True
)


def sana_Buttins():
    buttin = ReplyKeyboardMarkup(row_width=2,resize_keyboard=True)
    for buttins in sana():
        buttin.insert(KeyboardButton(text=buttins))
    buttin.insert(KeyboardButton(text="Bosh menu"))

    return buttin



bekorqilish = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🚫 Bekor qilish"),

        ],

    ],
    resize_keyboard=True
)