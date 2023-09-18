from time import sleep


def vstup_int(txt) -> int:
    while True:
        try:
            x: int = int(input(txt))
        except ValueError:
            print("Zadejte prosím číslo", end="\r")
            sleep(1)
            print("                    ", end="\r")
        else:
            return x


pocet_zamestnancu: int = vstup_int("Zadejte počet zaměstnanců: ")
mzdy: list = []

for i in range(pocet_zamestnancu):
    mzdy.append(vstup_int(f"Zadejte plat zaměstnance {i + 1}: "))
    print(f"Zadali jste plat {mzdy[i]} Kč", end="\r")
    sleep(0.5)
    print("                               ", end="\r")

print(f"Průměrný plat je {sum(mzdy) / len(mzdy)} Kč")

print(f"Počet mezd pod 10 000: {len([x for x in mzdy if x < 10000])}")
