"""
Это меню для авторизованного пользователя
"""
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

from utils.db_api.commands import get_new_message_user, get_new_events_user, get_new_notifications_user

btn_main_menu_user_auth_cd = CallbackData("btn_main_menu_user_auth", "action")# кнопка главное меню
btn_main_menu_user_auth = InlineKeyboardMarkup(row_width=1)
btn_main_menu_user_auth.insert(InlineKeyboardButton(text="Главное меню", callback_data="btn_main_menu_user_auth:main_menu_user_auth"))


menu_user_auth_cd = CallbackData("show_menu", "action") # основное меню пользователя
def make_callback_data(action):
    return menu_user_auth_cd.new(action=action)

async def menu_user_auth_jobseeker(telegram_id): # для соискателей
    menu_user_auth = InlineKeyboardMarkup(row_width=2)

    menu_user_auth.insert(InlineKeyboardButton(text="Полная информация", callback_data=make_callback_data(action="show_all_resume")))
    menu_user_auth.row(InlineKeyboardButton(text=f"Сообщения {await get_new_message_user(telegram_id)}".replace("None", ""),callback_data=make_callback_data(action="show_all_message")))
    menu_user_auth.insert(InlineKeyboardButton(text=f"Уведомления {await get_new_notifications_user(telegram_id)}".replace("None", ""), callback_data=make_callback_data(action="show_all_notifications")))
    menu_user_auth.insert(InlineKeyboardButton(text="Поиск", callback_data=make_callback_data(action="show_all_search")))
    menu_user_auth.insert(InlineKeyboardButton(text=f"События {await get_new_events_user(telegram_id)}".replace("None", ""), callback_data=make_callback_data(action="show_all_events")))
    menu_user_auth.insert(InlineKeyboardButton(text="Настройки", callback_data=make_callback_data(action="show_all_setting")))
    menu_user_auth.insert(InlineKeyboardButton(text="Выход", callback_data=make_callback_data(action="user_exit")))

    return menu_user_auth

async def menu_user_auth_other(telegram_id): # для соискателей
    menu_user_auth = InlineKeyboardMarkup(row_width=2)
    menu_user_auth.insert(InlineKeyboardButton(text="Полная информация", callback_data=make_callback_data(action="show_all_resume")))
    menu_user_auth.row(InlineKeyboardButton(text=f"Разместить вакансию",callback_data=make_callback_data(action="place_vacancy")))
    menu_user_auth.insert(InlineKeyboardButton(text=f"Разместить событие",callback_data=make_callback_data(action="place_event")))
    menu_user_auth.row(InlineKeyboardButton(text=f"Сообщения {await get_new_message_user(telegram_id)}".replace("None", ""),callback_data=make_callback_data(action="show_all_message")))
    menu_user_auth.insert(InlineKeyboardButton(text=f"Уведомления {await get_new_notifications_user(telegram_id)}".replace("None", ""), callback_data=make_callback_data(action="show_all_notifications")))
    menu_user_auth.insert(InlineKeyboardButton(text="Поиск", callback_data=make_callback_data(action="show_all_search")))
    menu_user_auth.insert(InlineKeyboardButton(text=f"События {await get_new_events_user(telegram_id)}".replace("None", ""), callback_data=make_callback_data(action="show_all_events")))
    menu_user_auth.insert(InlineKeyboardButton(text="Настройки", callback_data=make_callback_data(action="show_all_setting")))
    menu_user_auth.insert(InlineKeyboardButton(text="Выход", callback_data=make_callback_data(action="user_exit")))

    return menu_user_auth

