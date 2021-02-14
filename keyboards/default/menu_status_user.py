from aiogram import types

keyboard=types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True, one_time_keyboard=True, row_width=2)
keyboard.add("Соискатель", "Образовательное учреждение", "Работодатель")