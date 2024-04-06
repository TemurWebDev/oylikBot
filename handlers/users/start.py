from aiogram import types 
from aiogram.types import ReplyKeyboardRemove
from aiogram.dispatcher.filters.builtin import CommandStart
from .baza import user, usercreate,update_user
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext
from keyboards.default.key import tel,BoshMenu
from keyboards.inline.inlinekey import tasdiqlash
import re
from .admin import rek_ha,rek_yoq
from loader import dp
from loader import bot



class User(StatesGroup):
    name = State()
    phone = State()
    passport = State()


class UserUpdate(StatesGroup):
    name = State()
    phone = State()
    passport = State()
    
    




@dp.message_handler(CommandStart())
async def start_user(message: types.Message):
    usertg = user(str(message.from_user.id))
    if usertg == 201:
        await message.answer(f"Salom {message.from_user.first_name} Ro'yhatdan o'ting!\n\nIsm familiya.")
        await User.name.set()
        
    else:
        await message.answer(f"Kerakli bo'limni tanlang",reply_markup=BoshMenu)

        



@dp.message_handler(state=User.name)
async def name(message: types.Message, state: FSMContext):
    name = message.text
    await state.update_data(
            {"name": name}
        )
    
    await message.answer('Nomer yuborish tugmasini bosing!',reply_markup=tel)
    
    await User.next()



@dp.message_handler(state=User.phone,content_types=types.ContentTypes.CONTACT)
async def phon(message: types.Message, state: FSMContext):
    phon = message.contact.phone_number
    await state.update_data(
            {"phon": str(phon)}
        )
    
    await message.answer('Pasport seriasini yuboring!\n\nNamuna: AC1234567',reply_markup=ReplyKeyboardRemove())

    await User.next()


@dp.message_handler(state=User.passport)
async def passport(message: types.Message, state: FSMContext):
    passportuser = message.text.strip()
    first_name = message.from_user.first_name
    username = message.from_user.username
    user_id = message.from_user.id
    #passportuser = message.text
    regex_pattern = r'^[a-zA-Z]{2}\d{7}$'
    if re.match(regex_pattern, passportuser):
        await state.update_data({"passportuser": passportuser})
        


        data = await state.get_data()
        Ism = data.get('name')
        Tel = data.get('phon')
        passport = data.get('passportuser')

        habar = f"Yangi hodim\n\nIsm - {Ism}\nTel - {Tel}\nPassport - {passport}"
        

        try:
            usercreate(first_name=first_name,username=username,user_id=user_id,name=Ism,phon=Tel,passport=passport)
            await message.answer("Hush kelibsiz\n\nAdmin sizning shahsingizni tasdiqlagach oylik hisobotni ko'rolasiz!",reply_markup=BoshMenu)
            await bot.send_message(chat_id=1363350178,text=habar,reply_markup=tasdiqlash)
        except Exception as e:
            print(e)
        
        await state.finish()

    else:
        await message.reply("Noto'g'ri passport raqami formati. Iltimos, qaytadan kiriting.\n\nNamuna: AC1234567")

    



@dp.message_handler(text='/restat')
async def update_userTg(message:types.Message):
    userTg = user(str(message.from_user.id))
    if userTg['status'] == 'no_aktiv':
        await message.answer(f"Salom {message.from_user.first_name} Ro'yhatdan o'ting!\n\nIsm familiya.")
        await UserUpdate.name.set()
    else:
        await message.answer(f"Kerakli bo'limni tanlang",reply_markup=BoshMenu)
        

@dp.message_handler(state=UserUpdate.name)
async def nameUpdate(message: types.Message, state: FSMContext):
    name = message.text
    await state.update_data(
            {"name": name}
        )
    
    await message.answer('Nomer yuborish tugmasini bosing!',reply_markup=tel)
    
    await UserUpdate.next()



@dp.message_handler(state=UserUpdate.phone,content_types=types.ContentTypes.CONTACT)
async def phonUpdate(message: types.Message, state: FSMContext):
    phon = message.contact.phone_number
    await state.update_data(
            {"phon": str(phon)}
        )
    
    await message.answer('Pasport seriasini yuboring!\n\nNamuna: AC1234567',reply_markup=ReplyKeyboardRemove())

    await UserUpdate.next()



@dp.message_handler(state=UserUpdate.passport)
async def passportUpdate(message: types.Message, state: FSMContext):

    passportuser = message.text.strip()
    first_name = message.from_user.first_name
    username = message.from_user.username
    user_id = message.from_user.id
    user_up = user(str(user_id))
    regex_pattern = r'^[a-zA-Z]{2}\d{7}$'
    if re.match(regex_pattern, passportuser):
        await state.update_data({"passportuser": passportuser})
        


        data = await state.get_data()
        Ism = data.get('name')
        Tel = data.get('phon')
        passport = data.get('passportuser')

        habar = f"➕ Update \nYangi hodim\n\nIsm - {Ism}\nTel - {Tel}\nPassport - {passport}"
        

        try:
            update_user(id=user_up['id'],status='no_aktiv',first_name=first_name,username=username,user_id=str(user_id),name=Ism,phon=Tel,passport=passport)
            await message.answer("Hush kelibsiz\n\nAdmin sizning shahsingizni tasdiqlagach oylik hisobotni ko'rolasiz!",reply_markup=BoshMenu)
            await bot.send_message(chat_id=1363350178,text=habar,reply_markup=tasdiqlash)
        except Exception as e:
            print(e)
        
        await state.finish()

    else:
        await message.reply("Noto'g'ri passport raqami formati. Iltimos, qaytadan kiriting.\n\nNamuna: AC1234567")

    