from random import randint

seznam: list[int] = [randint(1, 6) for _ in range(6)]
seznam.sort()
if seznam == [1, 2, 3, 4, 5, 6]:
    print("Padla postupka")
else:
    print("Nepadla postupka")
