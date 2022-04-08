from functools import wraps


def authenticate(check: bool, i: int) -> bool:
    """

    :param check: bool
    :param i: int
    :return: bool
    """
    if check:
        print("Вы в системе!")
        return True
    else:
        print("Не правильное имя или пароль.")
        print(f"У вас осталось попыток: {i}." if i else "Попытки истекли!")
    return False


def check_password(data: dict, username: str, password: str) -> bool:
    """
    It accepts a dictionary of usernames and their passwords,
    and username and password that the user entered as strings.
    Checks if the user is in the dictionary (key) and
    if the password matches (value).
    Returns TRUE if the username is in the dictionary and the password matches,
    otherwise FALSE.
    :param data: dict
    :param username: str
    :param password: str
    :return: bool
    """
    return True if (username in data) and (data.get(username) == password) \
        else False


def login_wrapper_with_args(*args, **_kwargs):
    def login_wrapper(func):
        @wraps(func)
        def wrapper():
            for i in reversed(range(3)):    # loop to check the number
                func()                      # of login attempts
                usernames_and_passwords = args[0]
                check = check_password(usernames_and_passwords,
                                       username,
                                       password)
                result = authenticate(check, i)
                if result == 1:             # in case of a successful attempt
                    break                   # break
            return result

        return wrapper

    return login_wrapper


data = {"qwerty": "qwerty",     # не получилось вызвать словарь
        "lol": "123456789",     # не объявив его перед декоратором
        "admin": "admin"}


@login_wrapper_with_args(data)
def login() -> bool:
    """
    Receives input data through user input and declares in global variables,
    returns a boolean value in case of successful data input
    (always returns TRUE if there is no username and password verification).
    :return: bool
    """
    global username, password
    username = input("Name:")
    password = input("Password:")
    return True


if __name__ == '__main__':
    login()
