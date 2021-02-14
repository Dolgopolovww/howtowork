from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery
from aiogram.utils.markdown import hitalic

from keyboards.inline.menu_user_setting import menu_user_setting_cd, menu_user_setting_contact_data, \
    menu_user_navigation_setting_contact
from loader import dp
from utils.db_api.commands import update_user_contact_data


@dp.callback_query_handler(menu_user_setting_cd.filter(action="contact_data"))  # изменение контактных данных
async def edit_contact_data(call: CallbackQuery):
    await call.message.edit_text(text="Выберите, какие контактные данные вы бы хотели изменить",
                                 reply_markup=menu_user_setting_contact_data)
    await call.answer(text="")


@dp.callback_query_handler(menu_user_setting_cd.filter(action="edit_phone"))
async def edit_contact_data_phone(call: CallbackQuery, state: FSMContext):
    await call.message.edit_text(text="Укажите свой новый телефон \n\n" +
                                      hitalic("если хотите отменить действие, выберите команду /cancel"))
    await state.set_state("state_edit_phone")
    await call.answer(text="")


@dp.message_handler(state="state_edit_phone")
async def save_new_phone(message: types.Message, state: "FSMContext"):
    await update_user_contact_data(telegram_id=message.from_user.id, type="edit_phone",
                                   phone_or_email_or_address=int(message.text))
    await state.finish()
    await message.answer("Данные успешно изменены", reply_markup=menu_user_navigation_setting_contact)


@dp.callback_query_handler(menu_user_setting_cd.filter(action="edit_email"))
async def edit_contact_data_email(call: CallbackQuery, state: FSMContext):
    await call.message.edit_text(text="Укажите свой новый email \n\n" +
                                      hitalic("если хотите отменить действие, выберите команду /cancel"))
    await state.set_state("state_edit_email")
    await call.answer(text="")


@dp.message_handler(state="state_edit_email")
async def save_new_email(message: types.Message, state: FSMContext):
    await update_user_contact_data(telegram_id=message.from_user.id, type="edit_email", phone_or_email_or_address=message.text)
    await message.answer(text="Данные успешно изменены", reply_markup=menu_user_navigation_setting_contact)
    await state.finish()



@dp.callback_query_handler(menu_user_setting_cd.filter(action="edit_address"))
async def edit_contact_data_address(call: CallbackQuery, state: FSMContext):
    await call.message.edit_text(text="Укажите свой новый адресс \n\n" +
                                      hitalic("если хотите отменить действие, выберите команду /cancel"))
    await state.set_state("state_edit_address")
    await call.answer(text="")


@dp.message_handler(state="state_edit_address")
async def save_new_address(message: types.Message, state: FSMContext):
    await update_user_contact_data(telegram_id=message.from_user.id, type="edit_address", phone_or_email_or_address=message.text)
    await message.answer(text="Данные успешно изменены", reply_markup=menu_user_navigation_setting_contact)
    await state.finish()
