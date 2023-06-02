def vstup_f(txt):
    """Vstupní funkce"""
    while True:
        try:
            cislo = float(input(txt))
            return cislo
        except ValueError:
            print("Neplatná hodnota")


r = vstup_f("Zadejte průměr válce: ") / 2
h = vstup_f("Zadejte výšku válce: ")
print(
    "Objem válce je: {} a Povrch válce je: {}".format(
        round(3.14159265 * r ** 2 * h, 2), round(2 * 3.14159265 * r * (r + h), 2)
    )
)
