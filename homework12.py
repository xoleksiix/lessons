def arithmetic(a, b, operator):
    """
    Simple arithmetic function.
    The function takes two integers (a and b)
    and performs an operation on the operator.
    :param a: int
    :param b: int
    :param operator: str
    :return: result of operation or error.
    """
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        if b == 0:
            return "Делить на ноль нельзя!"
        else:
            return a / b
    else:
        return "Неизвестная операция."


if __name__ == '__main__':
    print(arithmetic(int(input("Введите первое число:")),
                     int(input("Введите второе число:")),
                     input("Введите символ операции над числами:")))
