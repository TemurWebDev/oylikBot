import logging
from aiogram import types
from data.config import ADMINS
from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton
from loader import bot, dp
from utils.misc import subscription
from data.config import CHANNELS
from .baza import user









@dp.callback_query_handler(text="check_subs")
async def checker(call: types.CallbackQuery):
    result = str()
    btn = InlineKeyboardMarkup()
    final_status = True
    for channel in CHANNELS:
        status = await subscription.check(user_id=call.from_user.id,
                                              channel=channel)
        final_status *= status
        channel = await bot.get_chat(channel)
        if not status:
            invite_link = await channel.export_invite_link()
            btn.add(InlineKeyboardButton(text=f"❌ {channel.title}", url=invite_link))

    btn.add(InlineKeyboardButton(text="♻️Obunani tekshirish", callback_data="check_subs"))
    if final_status:
        if user(str(call.from_user.id)) == 201:
            await call.message.answer("Assalomu alaykum! /start buyrug'ini qaytadan yuboring va ruyhatdan o'ting!")
        else:
            await call.message.answer("Assalomu alaykum! Kerakli bo'limni tanlang")

        await call.message.delete()
        
    if not final_status:
        await call.answer('Kanalga obuna bolishingiz kerak!', cache_time=0.05, show_alert=True)



@dp.callback_query_handler(text="check_subs",state='*')
async def checker(call: types.CallbackQuery):
    result = str()
    btn = InlineKeyboardMarkup()
    final_status = True
    for channel in CHANNELS:
        status = await subscription.check(user_id=call.from_user.id,
                                              channel=channel)
        final_status *= status
        channel = await bot.get_chat(channel)
        if not status:
            invite_link = await channel.export_invite_link()
            btn.add(InlineKeyboardButton(text=f"❌ {channel.title}", url=invite_link))

    btn.add(InlineKeyboardButton(text="♻️Obunani tekshirish", callback_data="check_subs"))
    if final_status:
        await call.message.answer("Assalomu alaykum! Kerakli bo'limni tanlang")
        await call.message.delete()
    if not final_status:
        await call.answer('Kanalga obuna bolishingiz kerak!', cache_time=0.05, show_alert=True)