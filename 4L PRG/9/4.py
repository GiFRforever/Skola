def vstup_int(txt, min):
    while True:
        try:
            cislo = int(input(txt))
            if cislo < min:
                print("Zadejte číslo větší než", min - 1)
            else:
                return cislo
        except ValueError:
            print("Zadejte celé číslo!")


od = vstup_int("Zadejte kladné celé číslo: ", 1)
with open("cisla.txt", "w") as cisla:
    for i in range(od, 0, -1):
        print(i)
        cisla.write(str(i) + "\n")

    suma = int(od * (od + 1) / 2)
    print("-" * len(str(suma)))
    print(suma)
    cisla.write("-" * len(str(suma)) + "\n")
    cisla.write(str(suma))
