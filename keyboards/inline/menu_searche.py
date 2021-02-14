"""
Это меню поиска вакансий, соискателей, работодателей.
"""
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

menu_user_auth_all_search_cd = CallbackData("show_menu_all_search", "type")
menu_user_auth_all_search = InlineKeyboardMarkup(row_width=1)

menu_user_auth_all_search.insert(InlineKeyboardButton(text="Вакансии", callback_data="show_menu_all_search:vacancies"))
menu_user_auth_all_search.insert(InlineKeyboardButton(text="Соискатели", callback_data="show_menu_all_search:job_seeker"))
menu_user_auth_all_search.insert(InlineKeyboardButton(text="Работодатель", callback_data="show_menu_all_search:employer"))
menu_user_auth_all_search.insert(InlineKeyboardButton(text="Образовательные учреждения",callback_data="show_menu_all_search:educational_institutions"))
menu_user_auth_all_search.insert(InlineKeyboardButton(text="Главное меню", callback_data="btn_main_menu_user_auth:main_menu_user_auth")) # вернуться в главное меню


navigation_btn_search = InlineKeyboardMarkup(row_width=1)
navigation_btn_search.insert(InlineKeyboardButton(text="Назад", callback_data="show_menu:show_all_search"))
navigation_btn_search.insert(InlineKeyboardButton(text="Главное меню", callback_data="btn_main_menu_user_auth:main_menu_user_auth"))