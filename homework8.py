import random

x = int(input("Рост Пети:"))
xlst = [random.randint(120, 200) for _ in range(22)]
xlst.sort(reverse=True)

for i in range(len(xlst)):
    if x == xlst[i]:        #есть ребята с таким же ростом как у Пети
        for j in range(i + 1, len(xlst)):
            if xlst[i] != xlst[j]:
                print(f"Петя по порядку #{j + 1}")
                break
        break
    elif x > xlst[i]:
        print(f"Петя по порядку #{i + 1}")
        break
    else:                   #если Петя ниже всех
        print(f"Петя по порядку #{len(xlst) + 1}")
        break