from random import shuffle


def štastných10() -> list[int]:
    čísla: list[int] = [i for i in range(1, 81)]
    shuffle(čísla)
    return sorted(čísla[:10])


print(*štastných10(), sep=", ")
