from aiogram import types
from loader import dp
from .baza import user,oylik,sana
from keyboards.default.key import Oylik,sana_Buttins,BoshMenu





@dp.message_handler(text='Bosh menu')
async def bosh_menu(message: types.Message):
    await message.answer("Kerakli bo'limni tanlang!",reply_markup=BoshMenu)





@dp.message_handler(text='🙎🏻‍♂️ My accaunt')
async def my_accaunt(message: types.Message):
    user_id = message.from_user.id
    my_accaunt = user(str(user_id))

    if my_accaunt['status'] == 'aktiv':
        holat = 'activ ✅'
    else:
        holat = 'no activ ❌'

    msg = f"My accaunt\n\n"
    msg+= f"💬 ISM : {my_accaunt['name']}\n"
    msg+= f"📞 Tel : +{my_accaunt['phone']}\n"
    msg+= f"📊 Holat : {holat}"
    
    
    await message.answer(msg)



@dp.message_handler(text='💰 Oylik')
async def my_accaunt(message: types.Message):


    await message.answer(f"Oyni tanlang!",reply_markup=sana_Buttins())


def oylik_hisobot(user_id,oy):
    try:
        
        oylik_user = oylik(str(user_id),oy)
        

        beriladi = f"{(oylik_user['jami_oylik'] + oylik_user['karobka_puli'] + oylik_user['bonus']+ oylik_user['kpi'] ) - (oylik_user['avans'] + oylik_user['avans_plastik']+ oylik_user['ishlamagan_kun'] + oylik_user['shtraf'] + oylik_user['forma'] + oylik_user['korpa_tushak'] + oylik_user['qushimcha']) } "

        msg = f"Oylik hisobot\n\n"
        msg+= f"🙎🏻‍♂️ Hodim : {oylik_user['user']['name']}\n\n"
        msg+= f"💵 Jami oylik: {oylik_user['jami_oylik']}\n"
        msg+= f"➕ Karobka puli : {oylik_user['karobka_puli']}\n"
        msg+= f"➕ Bonus : {oylik_user['bonus']}\n"
        msg+= f"➕ KPI : {oylik_user['kpi']}\n"
        msg+= f"➖ Avans : {oylik_user['avans']}\n"
        msg+= f"➖ Avans plastik : {oylik_user['avans_plastik']}\n"
        msg+= f"➖ Ishlamagan kun : {oylik_user['ishlamagan_kun']}\n"
        msg+= f"➖ Shtraf : {oylik_user['shtraf']}\n"
        msg+= f"➖ Forma : {oylik_user['forma']}\n"
        msg+= f"➖ Korpa tushak : {oylik_user['korpa_tushak']}\n"
        msg+= f"➖ Qoshimcha shtraf : {oylik_user['qushimcha']}\n\n"
        msg+= f"✅ Beriladi : {beriladi}"

        return msg
    except:
        return 'Malumotlar topilmadi!!'






data_oy = ['Yanvar','Fevral','Mart','Aprel','May','Iyun','Iyul','Avgust','Sentyabr','Oktyabr','Noyabr','Dekabr']

@dp.message_handler(text=data_oy)
async def my_accaunt(message: types.Message):

    
    user_id = message.from_user.id
    oy = message.text

    data = oylik_hisobot(user_id,oy)


    await message.answer(data)




