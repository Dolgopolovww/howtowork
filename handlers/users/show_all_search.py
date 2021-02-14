from aiogram.types import CallbackQuery
from aiogram.utils.markdown import hbold

from keyboards.inline.menu_searche import menu_user_auth_all_search_cd, menu_user_auth_all_search, navigation_btn_search
from keyboards.inline.menu_user_auth import menu_user_auth_cd, btn_main_menu_user_auth
from keyboards.inline.menu_user_setting import menu_user_setting
from loader import dp
from utils.db_api.commands import get_all_vacancy
from utils.give_info_users import give_info_users_certain_type


@dp.callback_query_handler(
    menu_user_auth_cd.filter(action="show_all_search"))  # показывает поиск в боте (вакансии, соискатели  и т.д.)
async def search_all_auth_user(call: CallbackQuery):
    await call.message.edit_text(text="Что бы вы хотели найти?", reply_markup=menu_user_auth_all_search)


@dp.callback_query_handler(menu_user_auth_all_search_cd.filter(type="vacancies"))  # показывает все вакансии
async def new_events_user(call: CallbackQuery):
    result_get_all_vacancy = await get_all_vacancy()
    text = hbold("Вакансии: \n\n")
    count = 1
    for i in result_get_all_vacancy:
        text += f"{count}. Описание: {i.vacancy}\nРазместил: {i.name_company}\n\n"
        count += 1
    await call.message.edit_text(text=text, reply_markup=btn_main_menu_user_auth)
    await call.answer(text="")


@dp.callback_query_handler(menu_user_auth_all_search_cd.filter(type="job_seeker"))  # показывает всех соискателей
async def all_jobseeker(call: CallbackQuery):
    text = await give_info_users_certain_type(
        "role_jobseeker")  # функция отдает данные о всех пользователях указанного статуса
    await call.message.edit_text(text=f"Ознакомьтесь с полным списком соискателей: \n\n {text}",
                                 reply_markup=navigation_btn_search)


@dp.callback_query_handler(menu_user_auth_all_search_cd.filter(type="employer"))  # показывает всех соискателей
async def all_employer(call: CallbackQuery):
    text = await give_info_users_certain_type("role_employers")
    await call.message.edit_text(text=f"Ознакомьтесь с полным списком работодателей: \n\n {text}",
                                 reply_markup=navigation_btn_search)


@dp.callback_query_handler(
    menu_user_auth_all_search_cd.filter(type="educational_institutions"))  # показывает всех соискателей
async def all_educational_institutions(call: CallbackQuery):
    text = await give_info_users_certain_type("role_education")
    await call.message.edit_text(text=f"Ознакомьтесь с полным списком образовательных учреждений: \n\n {text}",
                                 reply_markup=navigation_btn_search)


@dp.callback_query_handler(menu_user_auth_cd.filter(action="show_all_setting"))  # насторйки пользователя
async def all_setting_user(call: CallbackQuery):
    await call.message.edit_text(text=f"Выберите какие настройки вас интересуют: ", reply_markup=menu_user_setting)
