from functools import wraps


def authenticate(check: bool, i) -> bool:
    if check:
        print("Вы в системе!")
        return True
    else:
        print("Не правильное имя или пароль.")
        print(f"У вас осталось попыток: {i}." if i else "Попытки истекли!")
    return False


def check_password(data: dict, username: str, password: str) -> bool:
    return True if (username in data) and (data.get(username) == password) \
        else False


def login_wrapper_with_args(*args, **kwargs):
    print(args, kwargs)

    def login_wrapper(func):
        @wraps(func)
        def wrapper():
            for i in reversed(range(3)):
                func()
                usernames_and_passwords = args[0]
                check = check_password(usernames_and_passwords,
                                       username,
                                       password)
                result = authenticate(check, i)
                if result == 1:
                    break
            return result

        return wrapper

    return login_wrapper


data = {"qwerty": "qwerty",
        "second": "123456",
        "oldschol": "0000"}


@login_wrapper_with_args(data)
def login() -> bool:
    global username, password
    username = input("Name:")
    password = input("Password:")
    return True


if __name__ == '__main__':
    login()
