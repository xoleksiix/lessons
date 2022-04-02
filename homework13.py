def square(x):
    """
    The function takes one argument (the side of the square)
    and returns a tuple with three parameters: perimeter, area, and diagonal.
    :param x: int
    :return: tuple(int, int, float)
    """
    return x * 4, x ** 2, 2 ** 0.5 * x


if __name__ == '__main__':

    result = square(int(input("Введите сторону квадрата:")))
    print(f"Периметр: {result[0]}. "
          f"Площадь: {result[1]}. "
          f"Диагональ: {result[2]}.")
