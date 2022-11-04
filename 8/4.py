from random import randint


def vstup_f(txt):
    while True:
        try:
            vstup = float(input(txt))
            return vstup
        except ValueError:
            print("Neplatný vstup")

cislo = vstup_f("Zadejte číslo: ")
interval = [randint(20, 50), randint(20, 50)]
interval.sort()

if cislo >= interval[0] and cislo <= interval[1]:
    print(f"Číslo {cislo} je v intervalu <{interval[0]},{interval[1]}>")
else:
    print(f"Číslo {cislo} není v intervalu <{interval[0]},{interval[1]}>")