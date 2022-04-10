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


if __name__ == '__main__':
    data = {"user": "0000",
            "admin": "admin",
            "somebody": "qwerty"}
    attempt = 3  # кол-во попыток

    while attempt > 0:
        username_input = input("Имя:")
        password_input = input("Пароль:")
        if login(username_input, password_input):
            print("Вы в системе!")
            break
        attempt -= 1
        print("Не правильное Имя или Пароль")
        print(f"У вас осталось {attempt} попыток" if attempt != 0
              else "Попытки истекли!")
