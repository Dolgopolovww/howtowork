"""
Это меню  авторизованного пользователя
"""
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

menu_cd = CallbackData("show_menu", "action")
markup = InlineKeyboardMarkup(row_width=2)


user_btn_auth = InlineKeyboardButton(text="Авторизация", callback_data="show_menu:auth_user")
markup.insert(user_btn_auth)

user_btn_registration = InlineKeyboardButton(text="Регистрация", callback_data="show_menu:registration_user")
markup.insert(user_btn_registration)

visit_website_btn = InlineKeyboardButton(text="Перейти на сайт", callback_data="show_menu:visit_website", url="https://howtowork.ru/")
markup.insert(visit_website_btn)


come_back = InlineKeyboardMarkup()
come_back_btn = InlineKeyboardButton(text="Назад", callback_data="show_menu:come_back")
come_back.insert(come_back_btn)
