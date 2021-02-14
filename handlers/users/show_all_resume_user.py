from aiogram.types import CallbackQuery
from aiogram.utils.markdown import hbold, hitalic, hunderline

from keyboards.inline.menu_user_auth import menu_user_auth_cd, btn_main_menu_user_auth
from loader import dp
from utils.db_api.commands import select_all_inf_users


@dp.callback_query_handler(
    menu_user_auth_cd.filter(action="show_all_resume"))  # показать полную информацию о пользователе
async def show_all_resume_auth_user(call: CallbackQuery):
    await call.answer()
    all_information_user = await select_all_inf_users(
        telegram_id=call.from_user.id)  # получение всей информации зарегестрированного пользователя

    if all_information_user.role == "role_jobseeker":
        await call.message.edit_text(text=hunderline("Данные о вас: ") + "\n\n" +
                                          hbold("Имя: ") + f"{all_information_user.name} \n".replace("None", "Не указано") +
                                          hbold("Фамилия: ") + f"{all_information_user.surname} \n".replace("None", "Не указана") +
                                          hbold("Номер телефона: ") + f"{all_information_user.number_phone} \n".replace("None", "Не указан") +
                                          hbold("Адресс: ") + f"{all_information_user.address} \n".replace("None", "Не указан") +
                                          hbold("Email: ") + f"{all_information_user.email} \n\n".replace("None", "Не указан") +
                                          hitalic("Измеить персональные данные выможите в меню > настройки."),
                                     reply_markup=btn_main_menu_user_auth)
    elif all_information_user.role == "role_employers":
        await call.message.edit_text(text=hunderline("Данные о вас: ") + "\n\n" +
                                          hbold("Наименование компании: ") + f"{all_information_user.name_company} \n" +
                                          hbold("Имя: ") + f"{all_information_user.name} \n".replace("None", "Не указано") +
                                          hbold("Фамилия: ") + f"{all_information_user.surname} \n".replace("None", "Не указана") +
                                          hbold("Номер телефона: ") + f"{all_information_user.number_phone} \n".replace("None", "Не указан") +
                                          hbold("Адресс: ") + f"{all_information_user.address} \n".replace("None", "Не указан") +
                                          hbold("Email: ") + f"{all_information_user.email} \n\n".replace("None", "Не указан") +
                                          hbold("ОГРИП: ") + f"{all_information_user.ogrip} \n".replace("None", "Не указан") +
                                          hbold("ИНН: ") + f"{all_information_user.inn}\n\n".replace("None", "Не указан") +
                                          hitalic("Измеить персональные данные выможите в меню > настройки."),
                                     reply_markup=btn_main_menu_user_auth)
    else:
        await call.message.edit_text(text=hunderline("Данные о вас: ") + "\n\n" +
                                          hbold("Наименование компании: ") + f"{all_information_user.name_company} \n".replace("None", "Не указано") +
                                          hbold("Имя: ") + f"{all_information_user.name} \n".replace("None", "Не указано") +
                                          hbold("Фамилия: ") + f"{all_information_user.surname} \n".replace("None", "Не указана") +
                                          hbold("Номер телефона: ") + f"{all_information_user.number_phone} \n".replace("None", "Не указан") +
                                          hbold("Адресс: ") + f"{all_information_user.address} \n".replace("None", "Не указан") +
                                          hbold("Email: ") + f"{all_information_user.email} \n\n".replace("None", "Не указан") +
                                          hitalic("Измеить персональные данные выможите в меню > настройки."),
                                     reply_markup=btn_main_menu_user_auth)
