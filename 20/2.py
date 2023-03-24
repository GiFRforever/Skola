from random import randint
from math import prod


def vstup_int(txt) -> int:
    while True:
        try:
            cislo: int = int(input(txt))
            if cislo < 1:
                raise ValueError
            return cislo
        except ValueError:
            print("Nezadal jste číslo, zkuste to znovu.")


n: int = vstup_int("Zadejte počet čísel: ")
pole: list[int] = [randint(-10, 10) for _ in range(n)]
print("Čísla:", *pole)
print("Součin kladných: {}".format(prod([i for i in pole if i != 0])))
