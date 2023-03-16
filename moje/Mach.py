import platform, os, random as rd, sys

mach = False
body = []
povolené_true = ["1", "y", "a", "ano"]
povolené_false = ["0", "n", "ne"]
platná = [
    100,
    1200,
    200,
    31,
    32,
    300,
    41,
    42,
    43,
    400,
    51,
    52,
    53,
    54,
    500,
    61,
    62,
    63,
    64,
    65,
    600,
]
pravidla = """
Hráč A hodí dvěma kostkami, ale výsledek ukryje před hráčem B, který je na řadě. Svůj výsledek mu pouze oznámí. Hráč B má nyní dvě možnosti:

V případě pochybností může hráče A požádat o odkrytí vržených kostek. Pokud hráč A blafoval, hráč B získává bod a začíná nové kolo. Odpovídá-li oznámený výsledek hodnotě na kostkách, pak prohrává hráč požadující jejich odhalení.

V případě, že hráč B výsledku věří, převezme kostky s tím, že nyní musí na kostkách hodit vyšší hodnotu, než oznámil předchozí hráč. Může se však stát, že se mu to nepodaří. V takovém případě se pouze snaží předstírat, že předchozího hráče přehodil.
"""
postup = """
Na začátek zadejte počet hráčů. Minimální počet hráčů je 2 přičemž 1 je vždy počítač. Maximum není, ale od 6 hráčů je to už dost zdlouhavé.
Pro ztvrzení: pokud hráč dostane bod, vypije čtvrtku.
Při libovolné interakci s programem ve hře mužeš napsat "konec" a hra se ukončí.

1. Za hráče A hodí kostkami (klávesa Enter) a zobrazí mu jejich výsledek.
2. Hráč A se rozhodne jaké číslo oznámí hráči B a zadá ho.
    Jediná čísla co může zadat jsou 100, 200, 300, 400, 500, 600, 31, 32, 41, 42, 43,
      51, 52, 53, 54, 61, 62, 63, 64, 65, 1200.
3. Hráč B se rozhodne jestli věří hráči A nebo ne.
    Pokud ano, zadá "1", "y", "a" nebo "ano" a pokračuje dál svím hodem.
    Pokud ne, zadá "0", "n" nebo "ne". V tomto případě se odhalí jeho hod a pokud lhal,
      hráč A dostane bod, a pokud říkal pravdu, hráč B dostane bod. Pokračuje se dál hodem kostek.
"""

if (p := platform.uname()[0]) == "Windows":
    clear = lambda: os.system("cls")
elif p == "Linux":
    clear = lambda: os.system("clear")
else:
    exit("Nepodporovaný operační systém")


def počet_hráčů(txt):
    while True:
        vstup = input(txt)
        try:
            počet = int(vstup)
            if počet < 2:
                continue
            else:
                return počet
        except Exception:
            pass


def hod_kostkami():
    global mach
    kostka1 = rd.randint(1, 6)
    kostka2 = rd.randint(1, 6)
    if kostka2 > kostka1:
        kostka1, kostka2 = kostka2, kostka1
    if kostka2 == kostka1:
        hod = 100 * kostka1
        return hod
    elif kostka1 == 2:
        mach = True
        return 1200
    else:
        mach = False
        hod = 10 * kostka1 + kostka2
        return hod


def víra(txt):
    while True:
        vstup = input(txt)
        if vstup in povolené_true:
            return True
        elif vstup in povolené_false:
            return False
        elif vstup == "konec":
            konec()


def přehození(hod_minulý):
    vstup = ""
    while True:
        try:
            cislo = int(vstup := input("Co řeknete spoluhráči?: "))
            if cislo not in platná:
                print("Zadejte platné číslo")
                continue
            if cislo <= hod_minulý and not (cislo == hod_minulý == 1200):
                print("Musíš zadat větší číslo než", hod_minulý)
                continue
            return cislo
        except Exception:
            if vstup == "konec":
                konec()
            print("Zadejte platné číslo")


def konec():
    global body
    clear()
    for i, b in enumerate(body, start=1):
        print(f"Hrač {i} má {b} bodů")
    main()


def hra(hráčů):
    global body
    hod = 0
    body = [0] * hráčů
    hráč = 0
    while True:
        hod_minulý = hod
        if hráč == hráčů - 1:  # PC
            hod = hod_kostkami()
            if hod == 1200:
                lež = 1200
            elif hod <= hod_minulý:
                lež = rd.choice([p for p in platná if p > hod_minulý])
            else:
                lež = hod
            hráč = 0
        else:
            if input("Házej kostkami...") == "konec":
                konec()
            hod = hod_kostkami()
            if mach:
                print(f"Hráč {hráč+1}: Hodil jsi macháčka")
            print(f"Hráč {hráč+1}: Hodil jsi {hod}")
            lež = přehození(hod_minulý)
            hráč += 1
            if input(f"Předej hráči {hráč+1}... ") == "konec":
                konec()

        if hráč == hráčů - 1:  # PC
            clear()
            if lež > 54:  # nevěřím
                if lež == hod:
                    print(f"Hráč {hráč} nelhal, máš 1 bod")
                    body[hráč % hráčů] += 1
                else:
                    print(f"Hráč {hráč} lhal, hodil pouze {hod} a za to dostal 1 bod")
                    body[(hráč - 1) % hráčů] += 1
                hod = 0

            print("\n Průběžné skóre:")
            for i, b in enumerate(body, start=1):
                print(f"Hrač {i} má {b} bodů")
            input("\nPro pokračování stiskněte Enter...")
        else:
            clear()
            if not víra(f"Věříš hráči {hráč}, že hodil {lež}?: "):
                if lež == hod:
                    print(f"Hráč {hráč} nelhal, máš 1 bod")
                    body[hráč % hráčů] += 1
                else:
                    print(f"Hráč {hráč} lhal, hodil pouze {hod} a za to dostal 1 bod")
                    body[(hráč - 1) % hráčů] += 1
                hod = 0


def main():
    # menu: hra, pravidla, konec
    while True:
        print("Menu:")
        print("1: Hra")
        print("2: Pravidla")
        print("3: Postup hry")
        print("4: Konec")
        try:
            vstup = int(input("\nZvolte možnost: "))
            if vstup == 1:
                hra(počet_hráčů("Zadejte počet hráčů: "))
            elif vstup == 2:
                print(pravidla)
            elif vstup == 3:
                print(postup)
            elif vstup == 4:
                exit()
            else:
                print("Zadejte platné číslo")
                continue
        except Exception:
            print("Zadejte platné číslo")
            continue


if __name__ == "__main__":
    main()
