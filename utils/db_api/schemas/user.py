from sqlalchemy import Integer, Column, BigInteger, String, sql

from utils.db_api.db_gino import TimedBaseModel


class User(TimedBaseModel):
    __tablename__ = 'users_howtowork'
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    telegram_id = Column(Integer)
    token = Column(String(255))
    role = Column(String(100))
    name_company = Column(String(255))
    login = Column(String(100))
    password = Column(String(255))
    email = Column(String(100))

    new_message = Column(Integer)  # количество новых сообщений для пользователя
    new_notifications = Column(Integer)  # количество новых уведомлений пользователя
    new_events = Column(Integer)  # количество новый событий для пользователя

    name = Column(String(255))
    surname = Column(String(255))
    number_phone = Column(BigInteger)
    address = Column(String(255))

    ogrip = Column(BigInteger)
    inn = Column(BigInteger)

    query: sql.Select


class UserAuth(TimedBaseModel):
    __tablename__ = 'users_auth_in_bot'
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    telegram_id = Column(Integer)
    full_name = Column(String(255))
    token = Column(String(255))

    query: sql.Select


class Vacancy(TimedBaseModel):
    __tablename__ = 'vacancy'
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    vacancy = Column(String(1255))
    name_company = Column(String(500))

    query: sql.Select

class Events(TimedBaseModel):
    __tablename__ = 'events'
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    event = Column(String(1255))
    name_company = Column(String(500))
    date = Column(String(255))

    query: sql.Select