from random import randint


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
k = vstup_int("Zadejte horní limit: ")
pole: list[int] = [randint(1, 100) for _ in range(n)]
print("Čísla:", *pole)
print("Počet čísel menších než {}: {}".format(k, len([i for i in pole if i < k])))
