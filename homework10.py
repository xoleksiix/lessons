lst = input("Введите текст:").split()
d = {}

for i in range(len(lst)):
    if d.get(lst[i]) is None:
        d[lst[i]] = 1
    else:
        d[lst[i]] = d[lst[i]] + 1

for k, v in d.items():
    print(f"Слово {k} встречается {v} раз(a).")
