def vstup_f(txt):
    while True:
        try:
            vstup = float(input(txt))
            return vstup
        except ValueError:
            print("Neplatný vstup")


cislo = vstup_f("Zadejte číslo: ")
if cislo % 2 == 0:
    print("Číslo je sudé")
else:
    print("Číslo je liché")
