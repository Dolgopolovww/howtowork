from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

from utils.db_api.commands import get_new_message_user, get_new_events_user, get_new_notifications_user


menu_navigation_after_registr = InlineKeyboardMarkup(row_width=2)
menu_navigation_after_registr.insert(InlineKeyboardButton(text="Указать", callback_data="show_menu:show_all_setting"))
menu_navigation_after_registr.insert(InlineKeyboardButton(text="Пропустить..", callback_data="btn_main_menu_user_auth:main_menu_user_auth"))