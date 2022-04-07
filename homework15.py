from functools import wraps

def login_wrapper_with_args(*args, **kwargs):
    def login_wrapper(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            username_and_password = func()
            check = check_password(usernames_and_passwords,
                               username_and_password[0],
                               username_and_password[1])
            return authenticate(check)

        return wrapper()
    return login_wrapper()

@login_wrapper_with_args(usernames_and_passwords)
def login() -> tuple[str, str]:
    username = input("Name:")
    password = input("Password:")
    return username, password


def authenticate(check: bool) -> bool:
    i = 3
    while i > 0:
        if check:
            print("Вы в системе!")
            return True
        else:
            print("Не правильное имя или пароль.")
            i -= 1
            print(f"У вас осталось попыток: {i}." if i else "Попытки истекли!")
    return False


def check_password(data: dict, username: str, password: str) -> bool:
    return True if (username in data) and (data.get(username) == password) \
        else False


if __name__ == "__main__":
    usernames_and_passwords = {"first": "qwerty",
                               "second": "123456",
                               "oldschol": "0000"}

    login()

