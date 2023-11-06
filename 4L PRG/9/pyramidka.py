# print centered pyramid of height n
n = 100
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))
