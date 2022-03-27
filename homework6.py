import random

first = [random.randint(0, 9) for _ in range(10)]
second = [random.randint(0, 9) for _ in range(10)]

unique = [i for i in (first + second) if (first + second).count(i) == 1]

#print(first, second, unique)
print(f"Кол-во уникальных символов: {len(unique)}.")