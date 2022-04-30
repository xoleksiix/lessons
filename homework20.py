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
        return {"unknow": {"password": None, "last_fail_attempt": None}}
        # сделано для записи времени неудачных попыток
        # при логине, которого нет в списке зарегистрированых пользователей


def write_data(file_name: str, data: dict):
    with open(file_name, "w") as f:
        f.write(json.dumps(data))


def check_username(data, username):
    if data.get(username) is None:
        return "unknow"
    else:
        return username


def check_password(data: dict, username: str, password: str) -> bool:
    if data.get(username).get("password") != password:
        raise UserDoesNotExist("Wrong username or password!")
    return data.get(username).get("password") == password


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


def add_last_time_login(data, user):
    time_of_attempt = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    data.get(user).update({"last_fail_attempt": time_of_attempt})
    write_data("data.json", data)


def check_last_login(data, cd_for_login: int, username: str) -> int:
    user_data = data.get(username)
    if user_data.get("last_fail_attempt") is None:
        return 0
    last_time_login = datetime.strptime(user_data.get("last_fail_attempt"),
                                        "%m/%d/%Y, %H:%M:%S")
    return cd_for_login - ((datetime.now() - last_time_login).seconds // 60)


def parser():
    parser_args = argparse.ArgumentParser()
    parser_args.add_argument("-u", "--user", dest="username")
    parser_args.add_argument("-p", "--pass", dest="password")
    return parser_args.parse_args()


def registration(username: str, password: str):
    data = read_data("data.json")
    new_user = {
        username: {
            "password": password,
            "last_fail_attempt": None
        }
    }
    data.update(new_user)
    write_data("data.json", data)


if __name__ == '__main__':
    data = read_data("data.json")
    attempt = 3  # кол-во попыток
    cooldown_for_login = 5  # время для повторной попытки в минутах
    args = parser()
    username, password = args.username, args.password

    ask = input("Sing [in/up]? ")
    if ask.lower() == "up":
        while True:
            username = input("Username: ")
            if data.get(username):
                print("Username already taken!")
                continue
            else:
                password = input("Password: ")
                break
        registration(username, password)
        print("Registration successful. You are in the system!")
    elif ask.lower() == "in":
        while attempt > 0:
            username = username if username else input("Username: ")
            password = password if password else input("Password: ")
            username = check_username(data, username)
            if check_last_login(data, cooldown_for_login, username) > 0:
                print(f"You are blocked! Next try in "
                      f"{check_last_login(data, cooldown_for_login, username)} "
                      f"min.")
                break
            if login(username, password):
                print("You are in the system!")
                break
            else:
                attempt -= 1
                if attempt:
                    print(f"You have {attempt} attempt(s) left")
                else:
                    print("The attempts are over!")
                    add_last_time_login(data, username)
                username, password = None, None
    else:
        print("Incorrect input!")
