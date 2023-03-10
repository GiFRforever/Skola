from random import randint

seznam: list[int] = [randint(10, 99) for _ in range(20)]
print(*seznam)

seznam.sort()
print(*seznam)
