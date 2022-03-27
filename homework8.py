import random

xlst = [random.randint(120, 200) for _ in range(10)]
x = int(input("Рост Пети:"))

xlst.sort(reverse=True)
print(xlst)

for i in range(len(xlst)):
    if x == xlst[i]:
        for j in range(i + 1, len(xlst)):
            if xlst[i] != xlst[j]:
                print(f"Петя по порядку #{j + 1}")
                break
        break
    elif x > xlst[i]:
        print(f"Петя по порядку #{i + 1}")
        break
