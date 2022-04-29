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
        raise UserDoesNotExist("Wrong username or password!")
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
    data_of_logins = read_data("test/lasttimelogin.json")
    last_time_login = {user: datetime.now().strftime("%m/%d/%Y, %H:%M:%S")}
    data_of_logins.update(last_time_login)
    write_data("test/lasttimelogin.json", data_of_logins)


def check_last_login(cd_for_login: int, username) -> int:
    data_of_logins = read_data("test/lasttimelogin.json")
    if data_of_logins.get(username) is None:
        return 0
    last_time_login = datetime.strptime(data_of_logins.get(username),
                                        "%m/%d/%Y, %H:%M:%S")
    return cd_for_login - ((datetime.now() - last_time_login).seconds // 60)


def parser():
    parser_args = argparse.ArgumentParser()
    parser_args.add_argument("-u", "--user", dest="username")
    parser_args.add_argument("-p", "--pass", dest="password")
    return parser_args.parse_args()


def registration(username: str, password: str):
    data = read_data("test/data.json")
    data.update({username: password})
    write_data("test/data.json", data)


if __name__ == '__main__':
    data = read_data("test/data.json")
    attempt = 3  # кол-во попыток
    cooldown_for_login = 5  # время для повторной попытки в минутах
    args = parser()
    username, password = args.username, args.password

    while attempt > 0:
        if attempt == 3:
            ask = input("Sing [in/up]? ")
            if ask.lower() == "up":
                while True:
                    username = input("Username: ")
                    password = input("Password: ")
                    if data.get(username):
                        print("Username already taken!")
                    else:
                        break
                registration(username, password)
                print("Registration successful. You are in the system!")
                break

        if (username or password) and attempt == 3:
            if username and check_last_login(cooldown_for_login, username) > 0:
                print(f"You are blocked! Next try in "
                      f"{check_last_login(cooldown_for_login, username)} "
                      f"min.")
                break

            if login(username if username else input("Username:"),
                     password if password else input("Password:")):
                print("You are in the system!")
            else:
                attempt -= 1
                print(f"You have {attempt} attempt(s) left")
                continue

        username = input("Username: ")
        password = input("Password: ")

        if check_last_login(cooldown_for_login, username) > 0:
            print(f"You are blocked! Next try in "
                  f"{check_last_login(cooldown_for_login, username)} "
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
                add_last_time_login(username)
