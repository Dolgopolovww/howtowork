import logging

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from handlers.users.start import send_welcome
from keyboards.inline.menu_keyboards import menu_cd
from loader import dp
from utils.db_api.commands import create_vacancy, select_all_inf_users


@dp.callback_query_handler(menu_cd.filter(action="place_vacancy"))
async def place_new_vacancy(call: CallbackQuery, callback_data: dict, state: FSMContext):
    logging.info(f"{callback_data=}")
    await call.message.edit_text(text="Опишите вашу вакансию\n"
                                      "Если вы хотите отменить действие введите /cancel")
    await state.set_state("save_new_vacancy")
    await call.answer(text="")


@dp.message_handler(state="save_new_vacancy")
async def save_new_vacancy(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["about_vacancy"] = message.text
    res = await select_all_inf_users(message.from_user.id)
    await create_vacancy(text_vacancy=data["about_vacancy"], name_company=res.name_company)
    await message.answer(text="Ваше вакансия принята")
    await state.finish()
    await send_welcome(message, state)
