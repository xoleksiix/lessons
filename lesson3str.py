s = input("Введите что нибудь:")
s1 = "Это строка в которую {} новую строку".format(s)

print(s1)

s2 = s1.replace(s, "замена в строке")

print(s2)
print(len(s2))

if s2.find("строка"):
    print("Да")
