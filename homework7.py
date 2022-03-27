import random

lst = [random.randint(0, 9) for _ in range(10)]
count = 0

for i in range(1, (len(lst)) - 1):
    if lst[i] > lst[i - 1] + lst[i + 1]:
        count += 1

print(lst, f"чисел, которые больше двух своих соседей {count}.")
