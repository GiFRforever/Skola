from os import system
from platform import uname
from time import sleep

P: str = uname()[0]


def vstup_list_int(txt: str) -> list[int]:
    er = lambda: (
        print("\33[91mZadejte prosím 3 celá čísla oddělená čárkami!!!\33[0m"),
        sleep(3),
        system("cls") if P == "Windows" else system("clear"),
    )
    while True:
        try:
            if len(l := [int(x) for x in input(txt).split(",")]) == 3:
                return l
            else:
                er()
        except ValueError:
            er()


l: list[int] = vstup_list_int("Zadejte 3 celá čísla oddělená čárkami: ")
print(f"Nejmenší číslo je {min(l)}")
