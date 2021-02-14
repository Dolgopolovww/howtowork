from utils.db_api.commands import get_all_users_given_type


async def give_info_users_certain_type(type_get_users):
    """
    получение статус полльзователей и возвращает всех пользователей этого статуса

    :param type_get_users: "role_jobseeker", "role_employers", "role_education"
    :return:
    """
    get_users_type = await get_all_users_given_type(type_get_users)
    text = ""
    count_user = 1
    if type_get_users == "role_jobseeker":
        for i in get_users_type:
            text += f"{count_user}. Имя: {i.name}".replace("None" or " ",
                                                           "Не указано") + f", Фамилия: {i.surname}".replace(
                "None", "Не указано") + f", Адрес: " + f"{i.address}".replace("None" or " ",
                                                                              "Не указано") + f", Номер телефона: {i.number_phone} \n\n".replace(
                "None", "Не указано")
            count_user += 1
    elif type_get_users == "role_education":
        for i in get_users_type:
            text += f"{count_user}. Наименование компании: {i.name_company}" f", Имя: {i.name}".replace("None",
                                                                                                        "Не указано") + f", Фамилия: {i.surname}".replace(
                "None", "Не указано") + f", Адрес: {i.address}".replace("None",
                                                                        "Не указано") + f", Номер телефона: {i.number_phone} \n\n".replace(
                "None", "Не указано")
            count_user += 1

    else:
        for i in get_users_type:
            text += f"{count_user}. Наименование компании: {i.name_company}" f", Имя: {i.name}".replace("None",
                                                                                                        "Не указано") + f", Фамилия: {i.surname}".replace(
                "None", "Не указано") + f", Адрес: {i.address}".replace("None",
                                                                        "Не указано") + f", Номер телефона: {i.number_phone}".replace(
                "None", "Не указано") + f", ИНН: {i.inn}".replace(
                "None", "Не указано")  + f", ОГРиП: {i.ogrip}\n\n".replace(
                "None", "Не указано")
            count_user += 1
    return text
