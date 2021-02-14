import asyncio

from data import config
from utils.db_api import commands
from utils.db_api.db_gino import db


async def test():
    await db.set_bind(config.POSTGRES_URI)
    await db.gino.drop_all()
    await db.gino.create_all()

    print("Добавляем пользователей")
    await commands.add_user(telegram_id=18484, role="role_jobseeker", login="qwerty", password="qwerty",
                            email="qwerty@gmail.com", name="Андрей", surname="Долгополов", number_phone=89132009515,
                            address="Норильск")
    await commands.add_user(telegram_id=68646, role="role_jobseeker", login="wasd", password="wasd",
                            email="wasd@gmail.com", name="Гоша", surname="Беспалов", number_phone=89135048622,
                            address="Кайеркан")
    await commands.add_user(telegram_id=23457, role="role_jobseeker", login="xyz", password="xyz",
                            email="xyz@gmail.com", name="Аркаша", surname="Батайский", number_phone=89031119826,
                            address="Талнах")
    await commands.add_user(telegram_id=12346, role="role_employers", login="1", password="1", name_company="Норком",
                            email="1@gmail.com", name="Генадий", surname="Гулиев", number_phone=89232055555,
                            address="Москва", ogrip=2785373455, inn=692862632)
    await commands.add_user(telegram_id=11666, role="role_employers", login="2", password="2", name_company="ИП Мрачный",
                            email="2@gmail.com", name="Саша", surname="Мрачный", number_phone=430721,
                            address="Грозный", ogrip=21348641235, inn=54564265)
    await commands.add_user(telegram_id=89456, role="role_employers", login="3", password="3", name_company="ЖЭК",
                            email="3@gmail.com", name="Низам", surname="Акаганесян", number_phone=89139004685,
                            address="Норильск", ogrip=123456789, inn=987654321)
    await commands.add_user(telegram_id=12122, role="role_education", login="нии", password="нии", name_company="нии",
                            email="нии@gmail.com", name="Богдан", surname="Хряк", number_phone=435689,
                            address="Норильск")
    await commands.add_user(telegram_id=11111, role="role_education", login="МГУ", password="МГУ", name_company="МГУ",
                            email="МГУ@gmail.com", name="Петр", surname="Голяков", number_phone=259484,
                            address="Москва")

    await commands.create_vacancy(text_vacancy="Нужен рабочий который будет выкидывать мусор", name_company="ООО Пора")
    await commands.create_vacancy(text_vacancy="На работу требуеться говноботокодер", name_company="ИП Мрачный")

    await commands.create_event(text_event="Хакатон", name_company="jetbrains", date="25.02.2021")



    print("Готово")


loop = asyncio.get_event_loop()
loop.run_until_complete(test())
