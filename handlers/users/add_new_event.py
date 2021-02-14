import logging

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from handlers.users.start import send_welcome
from keyboards.inline.menu_keyboards import menu_cd
from loader import dp
from utils.db_api.commands import create_event, select_all_inf_users


@dp.callback_query_handler(menu_cd.filter(action="place_event"))
async def place_new_event(call: CallbackQuery, callback_data: dict, state: FSMContext):
    logging.info(f"{callback_data=}")
    await call.message.edit_text(text="Опишите какое событие вы хотите провести\n"
                                      "Если вы хотите отменить действие введите /cancel")
    await state.set_state("about_event")
    await call.answer(text="")


@dp.message_handler(state="about_event")
async def date_event(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["about_event"] = message.text
    await message.answer(text="Укажите дату события\n"
                              "Если вы хотите отменить действие введите /cancel")
    await state.set_state("save_new_event")


@dp.message_handler(state="save_new_event")
async def save_new_event(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["date_event"] = message.text
    res = await select_all_inf_users(message.from_user.id)
    await create_event(text_event=data["about_event"], name_company=res.name_company, date=data["date_event"])
    await message.answer(text="Ваше событие принято")
    await state.finish()
    await send_welcome(message, state)
