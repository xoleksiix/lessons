xlst = [150, 193, 180, 170, 175]
x = int(input())

xlst.sort(reverse=True)

for i in range(len(xlst)):
    if x == xlst[i]:
        print(f"Петя по порядку #{i + 2}")
        break
    elif x > xlst[i]:
        print(f"Петя по порядку #{i + 1}")
        break
