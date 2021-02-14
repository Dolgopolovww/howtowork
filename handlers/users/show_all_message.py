from aiogram.types import CallbackQuery

from aiogram.types import CallbackQuery

from keyboards.inline.menu_user_auth import menu_user_auth_cd, btn_main_menu_user_auth
from loader import dp
from utils.db_api.commands import get_new_message_user


@dp.callback_query_handler(menu_user_auth_cd.filter(action="show_all_message"))
async def new_message_user(call: CallbackQuery):
    new_message = await get_new_message_user(telegram_id=call.from_user.id)
    if new_message == None:
        await call.message.edit_text(text="На данный момент у вас нет новых сообщений\n"
                                          "Но вы всегда можите перейти на сайт https://howtowork.ru/, и начать общение сами ",
                                     reply_markup=btn_main_menu_user_auth)
    else:
        await call.message.edit_text(
            text=f"У вас {new_message} новых сообщений, возможно когда-то вы сможите их тут прочесть, а пока перейдите на сайт https://howtowork.ru/",
            reply_markup=btn_main_menu_user_auth)
    await call.answer(text="")
