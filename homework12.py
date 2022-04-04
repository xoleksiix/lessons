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
    operation = {"+": a + b, "-": a - b, "*": a * b, "/": a / b if b != 0 else "На ноль делить нельзя."}
    return operation.get(operator, "Неизвестная операция.")


if __name__ == '__main__':
    print(arithmetic(int(input("Введите первое число:")),
                     int(input("Введите второе число:")),
                     input("Введите символ операции над числами:")))
