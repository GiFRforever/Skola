def vstup_f(txt):
    while True:
        try:
            vstup = float(input(txt))
            return vstup
        except ValueError:
            print("Neplatný vstup")

mi1 = 0
mi2 = 0

def vstup_l(txt):
    global mi1
    global mi2
    while True:
        try:
            vstupraw = input(txt)
            if vstupraw[0] == "(":
                mi1 = 1
            elif vstupraw[0] == "<":
                mi1 = 2
            else:
                raise ValueError
            vstupraw = vstupraw[1:]
            if vstupraw[-1] == ")":
                mi2 = 1
            elif vstupraw[-1] == ">":
                mi2 = 2
            else:
                raise ValueError
            vstupraw = vstupraw[:-1]
            vstup = list(float(x) for x in vstupraw.split(","))
            return vstup
        except ValueError:
            print("Neplatný vstup")

cislo = vstup_f("Zadejte číslo: ")
interval = vstup_l("Zadejte interval <x,y) : ")
interval.sort()

if mi1 == 1 and mi2 == 1:
    if cislo > interval[0] and cislo < interval[1]:
        print("Číslo je v intervalu")
    else:
        print("Číslo není v intervalu")
elif mi1 == 1 and mi2 == 2:
    if cislo > interval[0] and cislo <= interval[1]:
        print("Číslo je v intervalu")
    else:
        print("Číslo není v intervalu")
elif mi1 == 2 and mi2 == 1:
    if cislo >= interval[0] and cislo < interval[1]:
        print("Číslo je v intervalu")
    else:
        print("Číslo není v intervalu")
elif mi1 == 2 and mi2 == 2:
    if cislo >= interval[0] and cislo <= interval[1]:
        print("Číslo je v intervalu")
    else:
        print("Číslo není v intervalu")