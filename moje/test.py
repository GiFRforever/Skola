default = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
a = []
for _ in range(3):
    a.append(default.copy())
print(a)
a[0][2] = 100
print(a)
