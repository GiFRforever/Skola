from math import prod


def plus(*args):
    return sum(args)


def minus(*args):
    return args[0] - sum(args[1:])


def multiply(*args):
    return prod(args)


def divide(*args):
    return args[0] / prod(args[1:])


def vstup_float(txt) -> float:
    while True:
        try:
            return float(input(txt))
        except ValueError:
            print("Zadejte číslo!")


menu: list[str] = [
    "1 - Přičíst",
    "2 - Odečíst",
    "3 - Vynásobit",
    "4 - Vydělit",
    "Cokoliv jiného - Konec",
]
operace: dict[str, str] = {
    "1": "+",
    "2": "-",
    "3": "*",
    "4": "/",
}


def vstup_operant(txt) -> str:
    while True:
        print("\n", *menu, sep="\n", end="\n\n")
        operant: str = input(txt)
        if operant in ["+", "-", "*", "/", "="]:
            return operant
        elif operant in operace:
            return operace[operant]
        else:
            return "="


def vypocet(zapis: list) -> float:
    vysledek: float = zapis[0]
    for o, c in zip(zapis[1::2], zapis[2::2]):
        if o == "+":
            vysledek = plus(vysledek, c)
        elif o == "-":
            vysledek = minus(vysledek, c)
        elif o == "*":
            vysledek = multiply(vysledek, c)
        elif o == "/":
            vysledek = divide(vysledek, c)
    return vysledek


def main() -> None:
    zapis = [0, "+"]
    while True:
        temp_cislo: float = vstup_float("Zadejte číslo: ")
        if temp_cislo == 0 and zapis[-1] == "/":
            print("Nulou nelze dělit!")
            continue
        zapis.append(temp_cislo)
        print(vypocet(zapis[:-2:]), *zapis[-2:], "=", vypocet(zapis))
        temp_operant: str = vstup_operant("Zadejte operant: ")
        if temp_operant == "=":
            print("Výsledek:", vypocet(zapis))
            break
        else:
            zapis.append(temp_operant)


if __name__ == "__main__":
    main()
