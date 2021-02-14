"""
Блок регистрации пользователя
Доделать:
    Проверки
    Отправку данных на сервер

"""
from pprint import pprint

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import CallbackQuery
from aiogram.utils.markdown import hitalic

from handlers.users.start import send_welcome
from keyboards.default.menu_status_user import keyboard
from keyboards.inline.menu_after_registration import menu_navigation_after_registr
from keyboards.inline.menu_keyboards import menu_cd
from keyboards.inline.menu_user_auth import btn_main_menu_user_auth
from loader import dp
from states.registration_and_authorization_user import RegistrationUser
from utils.db_api.commands import add_user, add_auth_in_bot_user


@dp.callback_query_handler(menu_cd.filter(action="registration_user"))
async def reg_user(call: CallbackQuery, callback_data: dict):
    await call.message.edit_text(text="Вы выбрали регистрацию, для отмены введите команды /start")
    await call.message.answer("Выберите Вашу роль: ", reply_markup=keyboard)
    await RegistrationUser.status_user.set()
    await call.answer(text="")


@dp.message_handler(state=RegistrationUser.status_user)
async def enter_name_company_or_login(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if message.text == "Соискатель":
            data['role'] = "role_jobseeker"
        elif message.text == "Работодатель":
            data['role'] = "role_employer"
        else:
            data['role'] = "role_education"
        print(data["role"])
    if data["role"] == "role_jobseeker":
        await message.answer("Укажите логин: ")
        await RegistrationUser.login.set()
    else:
        await message.answer("Укажите наименование организации: ")
        await RegistrationUser.name_company.set()


@dp.message_handler(state=RegistrationUser.name_company)
async def enter_login_org(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["name_company"] = message.text
    await message.answer("Укажите логин: ")
    await RegistrationUser.login.set()


@dp.message_handler(state=RegistrationUser.login)
async def enter_password(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["login"] = message.text
    await message.answer("Укажите пароль:\n"+
                         hitalic("Пароль должен быть быльше 6 символов"))
    await RegistrationUser.password.set()


@dp.message_handler(state=RegistrationUser.password)
async def enter_email(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["password"] = message.text
    await message.answer("Укажите email:")
    await RegistrationUser.email.set()


@dp.message_handler(state=RegistrationUser.email)
async def save_information_user(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["email"] = message.text
    pprint(data.items())
    if data["role"] == "role_jobseeker":
        await add_user(telegram_id=message.from_user.id, role=data["role"], login=data["login"], password=data["password"], email=data["email"])
    else:
        await add_user(telegram_id=message.from_user.id, role=data["role"], login=data["login"], password=data["password"], email=data["email"], name_company=data["name_company"])
    await add_auth_in_bot_user(telegram_id=message.from_user.id, full_name=message.from_user.full_name, token="")
    await state.finish()
    await message.answer(f"Спасибо, за регистрацию\n"
                         f"Заполните пожалуйуста персональные и контактные данные", reply_markup=menu_navigation_after_registr)


