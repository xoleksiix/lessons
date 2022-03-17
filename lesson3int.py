a = int(input("Enter number:"))

b = int(((a % 10) * 100) + (a % 100 - a % 10) + ((a % 1000 - a % 100) / 100))

print(b)
