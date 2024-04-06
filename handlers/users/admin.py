from aiogram import types
import logging

from loader import dp
import asyncio

from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext
from keyboards.default.adminKey import adminpanel
from .baza import userget
from aiogram.types import ContentType
from keyboards.default.key import BoshMenu,bekorqilish
from keyboards.inline.inlinekey import tasdiqlash
from aiogram.types import CallbackQuery
from .baza import user,userget

from loader import bot

ADMINS = [1363350178]

@dp.message_handler(text="admin panel", user_id=1363350178)
async def adminPanel(message: types.Message):

    await message.answer('admin panel',reply_markup=adminpanel)



@dp.message_handler(chat_id=1363350178, text='users')
async def users(message: types.Message):
    countuser = userget()
    datauser = userget()[-45:]
    text = f"Interview Questions || Foydalanuvchilar soni: {len(countuser)}\n\n"
    for user in datauser:
        text += f"{user['id']}). || {user['first_name']} || @{user['username']} || {user['status']}\n"
    await message.answer(text)


class Reklama(StatesGroup):
    message = State()



class Fikr(StatesGroup):
    habar = State()


class Javob_qaytarish(StatesGroup):
    id = State()
    javob = State()



@dp.message_handler(text="🚫 Bekor qilish",state='*')
async def habar_end(message: types.Message, state: FSMContext):

    current_state = await state.get_state()
    if current_state is None:
        return
    logging.info('Cancelling state %r', current_state)

    await state.finish()

    await message.answer("Kerakli bo'limni tanlashingiz mumkun!", reply_markup=BoshMenu)




@dp.message_handler(text="reklama",user_id=ADMINS)
async def bot_start(message: types.Message):
    await message.answer("reklama yuboring")
    await Reklama.message.set()


@dp.message_handler(content_types=ContentType.ANY,state=Reklama.message)
async def answer_fullname(message: types.Message, state: FSMContext):
    habar = message.text

    await state.update_data(
        {"habar": habar}
    )
    data = await state.get_data()
    reklama = data.get("habar")

    msg = reklama
    users = userget()
    for user in users:
        user_id = user['user_id']
        try:
            await message.send_copy(chat_id=user_id)
            await asyncio.sleep(0.05)
        except Exception as e:
            await bot.send_message(chat_id=ADMINS[0],text=f"{e}")
    await bot.send_message(chat_id=ADMINS[0],text=f"Reklama yuborildi! ✅")
    await state.finish()



@dp.message_handler(text="🗯️ Fikr bildirish")
async def fikrqoldirish(message: types.Message):
    await message.answer("Taklif va murojaatlaringizni qoldirishingiz mumkin!",reply_markup=bekorqilish)
    await Fikr.habar.set()





@dp.message_handler(state=Fikr.habar)
async def message_user(message: types.Message, state: FSMContext):
    msg = f"{message.from_user.first_name}--@{message.from_user.username}--{message.from_user.id}\n\n"
    msg += f"Habar: -> {message.text}"
    await bot.send_message(chat_id=1363350178,text=msg)
    await state.finish()
    await message.answer("✔️Muvaffaqiyatli yuborildi!",reply_markup=BoshMenu)



@dp.message_handler(text="Javob")
async def Javob_berish(message: types.Message):
    await message.answer("javob yozish uchun chat_id kiriting:")
    await Javob_qaytarish.id.set()


@dp.message_handler(state=Javob_qaytarish.id)
async def answer_admin_id(message: types.Message, state: FSMContext):
    id = message.text
    await state.update_data(
        {"chat_id": id}
    )
    await message.answer("javob yozish uchun text kiriting:")
    await Javob_qaytarish.next()


@dp.message_handler(state=Javob_qaytarish.javob)
async def answer_admin_text(message: types.Message, state: FSMContext):
    text = message.text
    await state.update_data(
        {"text": text}
    )

    data = await state.get_data()
    user_id = data.get("chat_id")
    admin_text = data.get("text")


    try:
        await bot.send_message(chat_id=user_id,text=admin_text)

        await state.finish()
        await bot.send_message(chat_id=1363350178, text="✔️Muvaffaqiyatli yuborildi!")
    except Exception as e:
        await bot.send_message(chat_id=1363350178,text=f"Hato: {e}")
        await state.finish()



@dp.callback_query_handler(text="ha")
async def rek_ha(call: CallbackQuery):
    


    await bot.send_message(chat_id=1363350178,text="Accaunt tasdiqlandi ✅")
    await call.message.delete()



@dp.callback_query_handler(text="yoq")
async def rek_yoq(call: CallbackQuery):
    


    await bot.send_message(chat_id=1363350178,text="Accaunt tasdiqlanmadi ❌\n\nPassport seriasi tug'ri emas")
    await call.message.delete()
