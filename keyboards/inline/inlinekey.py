from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton


tasdiqlash = InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text='✅ Ha',callback_data='ha'),
        InlineKeyboardButton(text="❌ Yo'q",callback_data="yoq")
    ],
    ]
)