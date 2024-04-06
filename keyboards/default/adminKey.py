from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

adminpanel = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="users"),
            KeyboardButton(text="reklama"),

        ],
        [
            KeyboardButton(text="Javob")
        ]

    ],
    resize_keyboard=True
)
