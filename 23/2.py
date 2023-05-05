evidence: list[str] = []

menu = [
    "1 - Přidat do evidence",
    "2 - Smazat z evidence",
    "3 - Hledat v evidenci",
    "4 - Vypsat evidenci",
    "Cokoliv jiného - Konec",
]


def pridej(jmeno) -> None:
    evidence.append(jmeno)


def smaz(jmeno) -> None:
    if zjisti(jmeno):
        evidence.remove(jmeno)
    else:
        print("Nenalezeno", end="\n\n")


def zjisti(jmeno) -> bool:
    return jmeno in evidence


def vypis() -> None:
    evidence.sort()
    print(
        "\n".join([f"    {i}  {e}" for i, e in enumerate(evidence, start=1)]),
        end="\n\n",
    )


def main() -> None:
    while True:
        print(*menu, sep="\n", end="\n\n")
        volba: str = input("Vyberte možnost: ")
        if volba == "1":
            pridej(input("Zadejte jméno: "))
        elif volba == "2":
            smaz(input("Zadejte jméno: "))
        elif volba == "3":
            print(
                "Nalezeno" if zjisti(input("Zadejte jméno: ")) else "Nenalezeno",
                end="\n\n",
            )
        elif volba == "4":
            vypis()
        else:
            break


if __name__ == "__main__":
    main()
