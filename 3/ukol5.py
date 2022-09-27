def vstup(txt):
    bagr = None
    while bagr is None:
        try:
            bagr = float(input(txt))
            return bagr
        except:
            print("Vložte číslo!!")


cislo_1 = vstup("Zadejte první číslo: ")
cislo_2 = vstup("Zadejte druhé číslo: ")
cislo_3 = vstup("Zadejte třetí číslo: ")
cislo_4 = vstup("Zadejte čtvrté číslo: ")
cislo_5 = vstup("Zadejte páté číslo: ")
print(
    "Průměr a součet čísel {} a {} a {} a {} a {} je {} a {}".format(
        round(cislo_1, 2),
        round(cislo_2, 2),
        round(cislo_3, 2),
        round(cislo_4, 2),
        round(cislo_5, 2),
        round((cislo_1 + cislo_2 + cislo_3 + cislo_4 + cislo_5) / 5, 2),
        round(cislo_1 + cislo_2 + cislo_3 + cislo_4 + cislo_5, 2),
    )
)
