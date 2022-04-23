import argparse
from datetime import datetime
from functools import wraps


class UserDoesNotExist(Exception):
    pass


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
        return check_password(data, username, password) \
               & authenticate() & func(username, password)
    return wrapper


@login_wrapper
def login(username: str, password: str) -> bool:
    ...
    return True


def add_last_time_login():
    # заглушка для добавления времени последней попытки входа в файл/етс
    return


def check_last_login(cd_for_login: int) -> int:
    last_time_login = datetime.now()
    """
    last_time_login должен принимать с файла время последней
    неудачной попытки залогиниться, пока что имитация,
    что попытка была только что
    """
    return cd_for_login - ((datetime.now() - last_time_login).seconds // 60)


def parser():
    parser_args = argparse.ArgumentParser()
    parser_args.add_argument("-l", "--user", dest="username")
    parser_args.add_argument("-p", "--pass", dest="password")
    return parser_args.parse_args()


if __name__ == '__main__':
    data = {"user": "0000",
            "admin": "admin",
            "somebody": "qwerty"}
    attempt = 3  # кол-во попыток
    cooldown_for_login = 0  # время для повторной попытки в минутах
    args = parser()
    username, password = args.username, args.password

    while attempt > 0:
        if (username or password) and attempt == 3:
            try:
                login(username if username else input("Имя:"),
                     password if password else input("Пароль:"))
            except UserDoesNotExist as error:
                attempt -= 1
                print(error, f"У вас осталось {attempt} попыток")
                continue
            else:
                print("Вы в системе!")
                break

        if check_last_login(cooldown_for_login) > 0:
            print(f"Вы заблокированы! Следующая попытка через "
                  f"{check_last_login(cooldown_for_login)} мин.")
            break

        username_input = input("Имя:")
        password_input = input("Пароль:")
        try:
            login(username_input, password_input)
        except UserDoesNotExist as error:
            attempt -= 1
            print(error, f"У вас осталось {attempt} попыток")
        else:
            print("Вы в системе!")
            break

        if attempt == 0:
            print("Попытки истекли!")
            add_last_time_login()
