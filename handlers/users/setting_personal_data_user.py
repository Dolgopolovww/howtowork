from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery
from aiogram.utils.markdown import hitalic

from handlers.users.start import send_welcome
from keyboards.inline.menu_user_auth import menu_user_auth_cd, btn_main_menu_user_auth
from keyboards.inline.menu_user_setting import menu_user_setting, menu_user_setting_cd, menu_user_setting_personal_data, \
    menu_user_navigation_setting_personal
from loader import dp
from utils.db_api.commands import update_user_personal_data


@dp.callback_query_handler(menu_user_setting_cd.filter(action="personal_data"))  # изменение персональных данных
async def edit_personal_data(call: CallbackQuery):
    await call.message.edit_text(text="Выберите, что именно вы хотите отредактировать",
                                 reply_markup=menu_user_setting_personal_data)
    await call.answer(text="")


@dp.callback_query_handler(menu_user_setting_cd.filter(action="edit_name"))  # изменение имя
async def edit_personal_data_name(call: CallbackQuery, state: FSMContext):
    await call.message.edit_text(text="Укажите ваше новое имя\n\n"+
                                 hitalic("если хотите отменить действие, выберите команду /cancel"))
    await state.set_state("state_edit_name")
    await call.answer(text="")


@dp.message_handler(state="state_edit_name")
async def save_new_name_user(message: types.Message, state: "FSMContext"):
    await update_user_personal_data(telegram_id=message.from_user.id, type="edit_name",
                                             name_or_surname=message.text)
    await state.finish()
    await message.answer("Данные успешно изменены", reply_markup=menu_user_navigation_setting_personal)


@dp.callback_query_handler(menu_user_setting_cd.filter(action="edit_surname"))  # изменение имя
async def edit_personal_data_surname(call: CallbackQuery, state: FSMContext):
    await call.message.edit_text(text="Укажите ваше новое фамилию"+
                                 hitalic("если хотите отменить действие, выберите команду /cancel"))
    await state.set_state("state_edit_surname")
    await call.answer(text="")


@dp.message_handler(state="state_edit_surname")
async def save_new_surname_user(message: types.Message, state: "FSMContext"):
    await update_user_personal_data(telegram_id=message.from_user.id, type="edit_surname",
                                             name_or_surname=message.text)
    await state.finish()
    await message.answer("Данные успешно изменены", reply_markup=menu_user_navigation_setting_personal)
