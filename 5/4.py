def vstup_f(txt):
    while True:
        try:
            vstup = float(input(txt))
            return vstup
        except ValueError:
            print("Neplatný vstup")

a = vstup_f("Zadejte stranu a: ")
b = vstup_f("Zadejte stranu b: ")
c = vstup_f("Zadejte stranu c: ")

if a + b > c and a + c > b and b + c > a:
    print("Trojúhelník lze sestrojit")
else:
    print("Trojúhelník nelze sestrojit")