"""
Блок состояний для fsm пользователя при регистрации
"""

from aiogram.dispatcher.filters.state import StatesGroup, State


class RegistrationUser(StatesGroup):
    status_user = State()  # Выбрать кто ты, сискатель, работодатель или инст
    name_company = State()  # Указать наименование компаниии
    login = State()  # Указать логин
    password = State()  # Указать пароль
    email = State()  # Указать email

class AuthorizationUser(StatesGroup):
    login = State()  # Указать логин
    password = State()  # Указать пароль
