n = int(input("Введите размер фигуры(значение от центра до вершин):"))

for i in range(n):
    print("  " * (n - i - 1), i * " *", " * ", i * "* ",
          "  " * (n - i - 1), sep="")

for i in reversed(range(n - 1)):
    x = 1 if i else 0
    print("  " * (n - i - 1),
          " *" * x,
          (i - 1) * "  ",
          " * ",
          (i - 1) * "  ",
          "* " * x,
          "  " * (n - i - 1), sep="")