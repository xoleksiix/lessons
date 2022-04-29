import argparse
from datetime import datetime
from functools import wraps
import json


class UserDoesNotExist(Exception):
    pass


def read_data(file_name: str) -> dict:
    try:
        with open(file_name, "r") as f:
            return json.loads(f.read())
    except FileNotFoundError:
        return {}


def write_data(file_name: str, data: dict):
    with open(file_name, "w") as f:
        f.write(json.dumps(data))


def check_password(data: dict, username: str, password: str) -> bool:
    if data.get(username) != password:
        raise UserDoesNotExist("Неправильное имя или пароль.")
    return data.get(username) == password


def authenticate() -> bool:
    ...
    return True


def login_wrapper(func):
    @wraps(func)
    def wrapper(username, password):
        try:
            check_password(data, username, password)
        except UserDoesNotExist as error:
            print(error)
        else:
            return check_password(data, username, password) \
                   & authenticate() & func(username, password)

    return wrapper


@login_wrapper
def login(username: str, password: str) -> bool:
    ...
    return True


def add_last_time_login(user):
    data_of_logins = read_data("lasttimelogin.json")
    last_time_login = {user: datetime.now().strftime("%m/%d/%Y, %H:%M:%S")}
    data_of_logins.update(last_time_login)
    write_data("lasttimelogin.json", data_of_logins)


def check_last_login(cd_for_login: int, username) -> int:
    data_of_logins = read_data("lasttimelogin.json")
    if data_of_logins.get(username) is None:
        return 0
    last_time_login = datetime.strptime(data_of_logins.get(username),
                                        "%m/%d/%Y, %H:%M:%S")
    return cd_for_login - ((datetime.now() - last_time_login).seconds // 60)


def parser():
    parser_args = argparse.ArgumentParser()
    parser_args.add_argument("-l", "--user", dest="username")
    parser_args.add_argument("-p", "--pass", dest="password")
    return parser_args.parse_args()


# def ask_for_registration():
#     print("Вы не зарегестированы, хотите зарегистрироваться?")
#     reg = input("[Y/N]:")
#     if reg.lower() == "y":
#         return True
#     elif reg.lower() == "n":
#         return False
#     else:
#         print("Некорректный ввод, повторите.")
#         ask_for_registration()


def registration():
    username = input("Name:")
    password = input("Password:")
    data = read_data("data.json")
    data.update({username: password})
    write_data("data.json", data)



if __name__ == '__main__':
    data = read_data("data.json")
    attempt = 3  # кол-во попыток
    cooldown_for_login = 5  # время для повторной попытки в минутах
    args = parser()
    username, password = args.username, args.password

    while attempt > 0:
        if (username or password) and attempt == 3:
            if username and data.get(username) is None:
                ask_for_reg = input("Такого пользователя не существует, "
                                    "желаете зарегестрироваться? [Y/N]:")
                if ask_for_reg.upper() == "Y":
                    registration()
                    print("Вы в системе!")
                    break

            if username and check_last_login(cooldown_for_login, username) > 0:
                print(f"Вы заблокированы! Следующая попытка через "
                      f"{check_last_login(cooldown_for_login, username)} "
                      f"мин.")
                break

            if login(username if username else input("Имя:"),
                     password if password else input("Пароль:")):
                print("Вы в системе!")
            else:
                attempt -= 1
                print(f"У вас осталось {attempt} попыток")
                continue

        username = input("Имя:")
        password = input("Пароль:")

        # if attempt == 3 and data.get(username) is None:
        #     if ask_for_registration():
        #         print("Вы в системе!")
        #         break

        if check_last_login(cooldown_for_login, username) > 0:
            print(f"Вы заблокированы! Следующая попытка через "
                  f"{check_last_login(cooldown_for_login, username)} "
                  f"мин.")
            break

        if login(username, password):
            print("Вы в системе!")
            break

        attempt -= 1

        if attempt:
            print(f"У вас осталось {attempt} попыток")
        else:
            print("Попытки истекли!")
            add_last_time_login(username)
