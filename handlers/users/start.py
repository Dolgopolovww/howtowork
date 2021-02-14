"""
* как отправлять уведомления пользователям когда в БД обновляеться количество новых писем или сабытий ???
** сделать разные меню для админов и пользователей
"""
import logging
from typing import Union

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import state
from aiogram.dispatcher.filters.builtin import CommandStart, Command
from aiogram.types import CallbackQuery, Message
from aiogram.utils.markdown import hbold, hcode, hitalic, hunderline, hstrikethrough, hlink

from handlers.users.authorization import authorization_user
from keyboards.inline.menu_keyboards import markup, menu_cd
from keyboards.inline.menu_searche import menu_user_auth_all_search_cd, menu_user_auth_all_search, navigation_btn_search
from keyboards.inline.menu_user_auth import menu_user_auth_cd, btn_main_menu_user_auth, \
    btn_main_menu_user_auth_cd, menu_user_auth_jobseeker, menu_user_auth_other
from keyboards.inline.menu_user_setting import menu_user_setting, menu_user_setting_cd, menu_user_setting_personal_data, \
    menu_user_setting_contact_data
from loader import dp
from utils.db_api.commands import check_user_auth_bot, delete_user_auth_bot, select_all_inf_users, get_new_message_user, \
    get_all_users_given_type, update_user_personal_data, update_user_contact_data, get_all_vacancy, create_vacancy, \
    get_all_events
from utils.give_info_users import give_info_users_certain_type


@dp.message_handler(commands=["start", "cancel"], state="*")
@dp.callback_query_handler(btn_main_menu_user_auth_cd.filter(action="main_menu_user_auth"))
async def send_welcome(message: Union[CallbackQuery, Message], state: FSMContext, **kwargs):
    await state.finish()
    if await check_user_auth_bot(telegram_id=message.from_user.id) == None:
        await message.answer(text="Добро пожаловать на платформу HowToWork", reply_markup=markup)
    else:
        user = await select_all_inf_users(telegram_id=message.from_user.id)
        if user.role == "role_jobseeker":
            menu_user_auth = await menu_user_auth_jobseeker(message.from_user.id)
        else:
            menu_user_auth = await menu_user_auth_other(message.from_user.id)
        if isinstance(message, Message):
            await message.answer(hbold("Добро пожаловать, на платформу HowToWork\n\n")+
                                 f"Помощник в поиске работы и сотрудников\n"
                                 f"Проек в работе. Но вы можите с ним поиграться",
                                 reply_markup=menu_user_auth)

        elif isinstance(message, CallbackQuery):
            call = message
            await call.message.edit_text(text=hbold("Добро пожаловать, на платформу HowToWork\n\n")+
                                     f"Помощник в поиске работы и сотрудников\n"
                                     f"Проек в работе. Но вы можите с ним поиграться",
                                     reply_markup=menu_user_auth)
























@dp.callback_query_handler(menu_user_auth_cd.filter(action="show_all_events"))
async def show_events(call: CallbackQuery):
    text = hitalic("Я пока не знаю что именно тут будет отоброжаться\n"
                                              "Скорее всего хакатоны всякие, олимпиады, дни открытых дверей и т.д.\n"
                                              "Нужно уточнить будет\n\n") + ""
    all_events = await get_all_events()
    count = 1
    for i in all_events:
        text += f"{count}. Наименование события: {i.event}\n   Дата проведение: {i.date}\n   Наименование огранизаторов: {i.name_company}\n"
        count += 1
    await call.message.edit_text(text=text,
                                 reply_markup=btn_main_menu_user_auth)
    await call.answer(text="")







@dp.callback_query_handler(menu_cd.filter(action="auth_user"))
async def auth_user(call: CallbackQuery, callback_data: dict):
    await call.message.edit_text(text="Вы выбрали авторизацию, для отмены введите команды /start")
    await authorization_user(call.message)
    await call.answer(text="")


@dp.callback_query_handler(menu_user_auth_cd.filter(action="user_exit"))
async def exit_auth_user(call: CallbackQuery, state):
    await call.message.delete()
    await delete_user_auth_bot(telegram_id=call.from_user.id)
    await send_welcome(call.message, state)
    await call.answer(text="")





@dp.callback_query_handler(menu_user_auth_cd.filter(action="show_all_notifications"))
async def show_notifications(call: CallbackQuery):
    await call.message.edit_text(text=hitalic("Я пока не знаю что именно тут будет отоброжаться\n"
                                              "Нужно уточнить будет"), reply_markup=btn_main_menu_user_auth)
    await call.answer(text="")


