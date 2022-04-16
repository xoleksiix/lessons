import argparse
from datetime import datetime
from functools import wraps


def check_password(data: dict, username: str, password: str) -> bool:
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
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", dest="username")
    parser.add_argument("-p", dest="password")
    return parser.parse_args()


if __name__ == '__main__':
    data = {"user": "0000",
            "admin": "admin",
            "somebody": "qwerty"}
    attempt = 3  # кол-во попыток
    cooldown_for_login = 0  # время для повторной попытки в минутах
    username, password = parser().username, parser().password

    while attempt > 0:
        if check_last_login(cooldown_for_login) > 0:
            print(f"Вы заблокированы! Следующая попытка через "
                  f"{check_last_login(cooldown_for_login)} мин.")
            break
        else:
            username_input = username if username else input("Имя:")
            password_input = password if password else input("Пароль:")
            if login(username_input, password_input):
                print("Вы в системе!")
                break
            attempt -= 1
            if attempt:
                print(f"Неправильное имя или пароль. "
                      f"У вас осталось {attempt} попыток")
            else:
                print("Попытки истекли!")
                add_last_time_login()
