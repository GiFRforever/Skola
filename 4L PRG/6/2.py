a, b = 0, 1
for _ in range(int(input("Zadejte počet Fibonacciho čísel: "))):
    a, b = b, a + b
    print(a)
