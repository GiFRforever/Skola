def vstup_f(txt):
    while True:
        try:
            vstup = float(input(txt))
            return vstup
        except ValueError:
            print("Neplatný vstup")

c1 = vstup_f("Zadejte číslo: ")
c2 = vstup_f("Zadejte číslo: ")
if c1 > c2:
    print("První číslo je větší")
elif c1 < c2:
    print("Druhé číslo je větší")
else:
    print("Čísla jsou stejná")