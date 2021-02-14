"""
Блок авторизации пользователя
Доделать:
    Отправку данных на сервер

"""
from pprint import pprint

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import ReplyKeyboardRemove


from keyboards.inline.menu_user_auth import btn_main_menu_user_auth
from loader import dp
from states.registration_and_authorization_user import AuthorizationUser
from utils.db_api.commands import add_auth_in_bot_user, select_user, add_user


@dp.message_handler(Command("authorization"), state="*")
async def authorization_user(message: types.Message):
    await message.answer("Укажите логин: ", reply_markup=ReplyKeyboardRemove())
    await AuthorizationUser.login.set()

    @dp.message_handler(state=AuthorizationUser.login)
    async def enter_password(message: types.Message, state: FSMContext):
        async with state.proxy() as data:
            data["login"]=message.text
        await message.answer("Укажите пароль: ")
        await AuthorizationUser.password.set()

    @dp.message_handler(state=AuthorizationUser.password)
    async def save_information_user(message: types.Message, state: FSMContext):
        async with state.proxy() as data:
            data["password"]=message.text
        if await select_user(login=data["login"], password=data["password"]) != None:
            await add_auth_in_bot_user(telegram_id=message.from_user.id, full_name=message.from_user.full_name, token="")
            await message.answer("Спасибо, за регистрацию \nНажмите /start для выхода в главное меню или кнопку ниже", reply_markup=btn_main_menu_user_auth)
            await state.finish()

        else:
            await message.answer("Неверно введены данные")
            await authorization_user(message)
