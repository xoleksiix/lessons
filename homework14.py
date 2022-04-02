def multiplication_of_numbers(x):
    result = 1
    for i in str(x):
        result = int(i) * result if int(i) != 0 else result
    return result

if __name__ == '__main__':
    numbers = int(input("Введите число:"))
    print(f"Результат: {multiplication_of_numbers(numbers)}.")
