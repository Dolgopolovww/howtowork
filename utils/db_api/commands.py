from pprint import pprint

from asyncpg import UniqueViolationError

from utils.db_api.db_gino import db
from utils.db_api.schemas.user import User, UserAuth, Vacancy, Events


# Регистрация пользователя
async def add_user(telegram_id: int, role: str, login: str, password: str, email: str, new_message: int = 0, new_notifications: int = 0,
                   new_events: int = 0, token: str = None,
                   name_company: str = None,name: str = None, surname: str = None, number_phone: int = None,
                   address: str = None, ogrip: int = None, inn: int = None):
    try:
        user = User(telegram_id=telegram_id, role=role, login=login, password=password, email=email, token=token,
                    name_company=name_company, new_message=new_message, new_notifications=new_notifications,
                    new_events=new_events, name=name, surname=surname, number_phone=number_phone, address=address, ogrip=ogrip, inn=inn)
        await user.create()
    except UniqueViolationError:
        pass


# Авторизация пользователя  в боте
async def add_auth_in_bot_user(telegram_id: str, full_name: str, token: str = None):
    user_auth_in_bot = UserAuth(telegram_id=telegram_id, full_name=full_name, token=token)
    await user_auth_in_bot.create()




# Проверка, зарегстрирован ли пользователь
async def select_user(login, password):
    user = await User.query.where(User.login == login and User.password == password).gino.first()
    return user


# Есть ли telegram_id в БД авторизованных пользователей
async def check_user_auth_bot(telegram_id):
    user = await UserAuth.query.where(UserAuth.telegram_id == telegram_id).gino.first()
    return user


# Удаление пользователя из БД авторизованных пользователей в боте
async def delete_user_auth_bot(telegram_id):
    await UserAuth.delete.where(UserAuth.telegram_id == telegram_id).gino.status()
    await User.delete.where(User.telegram_id == telegram_id).gino.status()


async def select_all_inf_users(telegram_id):
    users = await User.query.where(User.telegram_id == telegram_id).gino.first()
    return users

async def get_new_message_user(telegram_id):
    new_message = await User.select('new_message').where(User.telegram_id == telegram_id).gino.scalar()
    print(new_message)
    if new_message >= 1:
        return f"({new_message})"


async def get_new_notifications_user(telegram_id):
    new_notifications = await User.select('new_notifications').where(User.telegram_id == telegram_id).gino.scalar()
    if new_notifications >= 1:
        return f"({new_notifications})"

async def get_new_events_user(telegram_id):
    new_events = await User.select('new_events').where(User.telegram_id == telegram_id).gino.scalar()
    if new_events >= 1:
        return f"({new_events})"


async def get_all_users_given_type (type):
    """
    :param type: "role_jobseeker", "role_employers", "role_education"
    """
    get_users_type = await User.query.where(User.role == type).gino.all()
    return get_users_type



async def update_user_personal_data(telegram_id, type, name_or_surname):
    user = await User.query.where(User.telegram_id == telegram_id).gino.first()
    if type == "edit_name":
        await user.update(name=name_or_surname).apply()
    else:
        await user.update(surname=name_or_surname).apply()


async def update_user_contact_data(telegram_id, type, phone_or_email_or_address):
    user = await User.query.where(User.telegram_id == telegram_id).gino.first()
    if type == "edit_phone":
        await user.update(number_phone=phone_or_email_or_address).apply()
    elif type == "edit_email":
        await user.update(email=phone_or_email_or_address).apply()
    else:
        await user.update(address=phone_or_email_or_address).apply()


async def create_vacancy(text_vacancy, name_company):
    new_vanacy = Vacancy(vacancy=text_vacancy, name_company=name_company)
    await new_vanacy.create()



async def get_all_vacancy():
    get_vacancy = await Vacancy.query.gino.all()
    return get_vacancy


async def create_event(text_event, name_company, date):
    new_event = Events(event=text_event, name_company=name_company, date=date)
    await new_event.create()

async def get_all_events():
    get_events = await Events.query.gino.all()
    return get_events