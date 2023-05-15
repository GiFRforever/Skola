def vstup_f(txt):
    """Vstupní funkce"""
    while True:
        try:
            vsthod = float(input(txt))
            return vsthod
        except ValueError:
            print("Neplatná hodnota")


def vstup_s(txt):
    """Vstupní funkce"""
    while True:
        try:
            vsthod = str(input(txt))
            return vsthod
        except ValueError:
            print("Neplatná hodnota")


první = vstup_s("Zadejte první produkt: ")
první_cena = vstup_f("Zadejte cenu prvního produktu: ")
druhý = vstup_s("Zadejte druhý produkt: ")
druhý_cena = vstup_f("Zadejte cenu druhého produktu: ")
třetí = vstup_s("Zadejte třetí produkt: ")
třetí_cena = vstup_f("Zadejte cenu třetího produktu: ")

print(
    "Za {}, {} a {} jsem utratil(a) {} Kč.".format(
        první, druhý, třetí, int(první_cena + druhý_cena + třetí_cena)
    )
)
