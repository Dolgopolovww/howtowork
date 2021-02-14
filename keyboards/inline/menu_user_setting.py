"""
Это меню настроек пользователя.
"""
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

menu_user_setting_cd = CallbackData("show_menu_setting", "action")
menu_user_setting = InlineKeyboardMarkup(row_width=1) # основное меню настройки пользователя

menu_user_setting.insert(InlineKeyboardButton(text="Личные данные", callback_data="show_menu_setting:personal_data"))
menu_user_setting.insert(InlineKeyboardButton(text="Контактные данные", callback_data="show_menu_setting:contact_data"))
menu_user_setting.insert(InlineKeyboardButton(text="Главное меню", callback_data="btn_main_menu_user_auth:main_menu_user_auth"))


menu_user_setting_personal_data =InlineKeyboardMarkup(row_width=1) # настройка персональных данных
menu_user_setting_personal_data.insert(InlineKeyboardButton(text="Изменить имя", callback_data="show_menu_setting:edit_name"))
menu_user_setting_personal_data.insert(InlineKeyboardButton(text="Изменить фамилию", callback_data="show_menu_setting:edit_surname"))
menu_user_setting_personal_data.insert(InlineKeyboardButton(text="Назад", callback_data="show_menu:show_all_setting"))
menu_user_setting_personal_data.insert(InlineKeyboardButton(text="Главное меню", callback_data="btn_main_menu_user_auth:main_menu_user_auth"))


menu_user_setting_contact_data =InlineKeyboardMarkup(row_width=1) # настройка контактных данных
menu_user_setting_contact_data.insert(InlineKeyboardButton(text="Изменить номер телефона", callback_data="show_menu_setting:edit_phone"))
menu_user_setting_contact_data.insert(InlineKeyboardButton(text="Изменить email", callback_data="show_menu_setting:edit_email"))
menu_user_setting_contact_data.insert(InlineKeyboardButton(text="Изменить адресс", callback_data="show_menu_setting:edit_address"))
menu_user_setting_contact_data.insert(InlineKeyboardButton(text="Назад", callback_data="show_menu:show_all_setting"))
menu_user_setting_contact_data.insert(InlineKeyboardButton(text="Главное меню", callback_data="btn_main_menu_user_auth:main_menu_user_auth"))


menu_user_navigation_setting_personal = InlineKeyboardMarkup(row_width=1)
menu_user_navigation_setting_personal.insert(InlineKeyboardButton(text="Назад", callback_data="show_menu_setting:personal_data"))
menu_user_navigation_setting_personal.insert(InlineKeyboardButton(text="Главное меню", callback_data="btn_main_menu_user_auth:main_menu_user_auth"))

menu_user_navigation_setting_contact = InlineKeyboardMarkup(row_width=1)
menu_user_navigation_setting_contact.insert(InlineKeyboardButton(text="Назад", callback_data="show_menu_setting:contact_data"))
menu_user_navigation_setting_contact.insert(InlineKeyboardButton(text="Главное меню", callback_data="btn_main_menu_user_auth:main_menu_user_auth"))