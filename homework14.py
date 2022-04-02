def multiplication_of_numbers(x):
    result = 1
    for i in str(x):
        result = int(i) * result if i != "0" else result
    return result

if __name__ == '__main__':
    print(multiplication_of_numbers(int(input("Введите число:"))))
