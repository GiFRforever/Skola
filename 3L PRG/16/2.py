from random import randint as ri

print("\na)")
for _ in range(10):
    print(f"{ri(1, 1000):<4} Kč")

print("\nb)")
for _ in range(10):
    print(f"{ri(1, 1000):>4} Kč")

print("\nc)")
for _ in range(10):
    print("{0:>4}.0 Kč   {0:>4} Kč".format(ri(1, 1000)))
