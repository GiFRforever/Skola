tělesa: list[str] = [
    "krychle",
    "kvádr",
    "hranol",
    "jehlan",
    "válec",
    "kužel",
    "koule",
]


def výpočet_objemu(těleso: str, strany: list[float]) -> float:
    if těleso == "krychle":
        return strany[0] ** 3
    elif těleso == "kvádr":
        return strany[0] * strany[1] * strany[2]
    elif těleso == "hranol":
        return strany[0] ** 2 * strany[1]
    elif těleso == "jehlan":
        return strany[0] ** 2 * strany[1] / 3
    elif těleso == "válec":
        return strany[0] ** 2 * strany[1] * 3.14
    elif těleso == "kužel":
        return strany[0] ** 2 * strany[1] * 3.14 / 3
    elif těleso == "koule":
        return strany[0] ** 3 * 3.14 * 4 / 3
    else:
        return 0


def výpočet_povrchu(těleso: str, strany: list[float]) -> float:
    if těleso == "krychle":
        return strany[0] ** 2 * 6
    elif těleso == "kvádr":
        return (
            strany[0] * strany[1] * 2
            + strany[0] * strany[2] * 2
            + strany[1] * strany[2] * 2
        )
    elif těleso == "hranol":
        return strany[0] ** 2 * 2 + strany[0] * strany[1] * 4
    elif těleso == "jehlan":
        return (
            strany[0] ** 2
            + (strany[0] / 2) * (strany[1] ** 2 + (strany[0] / 2) ** 2) ** 0.5 * 4
        )
    elif těleso == "válec":
        return strany[0] ** 2 * 2 * 3.14 + strany[0] * strany[1] * 2 * 3.14
    elif těleso == "kužel":
        return strany[0] ** 2 * 3.14 + strany[0] * strany[1] * 2 * 3.14
    elif těleso == "koule":
        return strany[0] ** 2 * 4 * 3.14
    else:
        return 0


def main() -> None:
    print("\nPodporovaná tělesa: " + ", ".join(tělesa))
    těleso: str = input("Zadej těleso: ")
    if těleso in tělesa:
        strany: list[float] = []
        if těleso == "krychle":
            strany.append(float(input("Zadej stranu: ")))
        elif těleso == "kvádr":
            strany.append(float(input("Zadej stranu a: ")))
            strany.append(float(input("Zadej stranu b: ")))
            strany.append(float(input("Zadej stranu c: ")))
        elif těleso == "hranol":
            strany.append(float(input("Zadej stranu a: ")))
            strany.append(float(input("Zadej výšku: ")))
        elif těleso == "jehlan":
            strany.append(float(input("Zadej stranu a: ")))
            strany.append(float(input("Zadej výšku: ")))
        elif těleso == "válec":
            strany.append(float(input("Zadej poloměr: ")))
            strany.append(float(input("Zadej výšku: ")))
        elif těleso == "kužel":
            strany.append(float(input("Zadej poloměr: ")))
            strany.append(float(input("Zadej výšku: ")))
        elif těleso == "koule":
            strany.append(float(input("Zadej poloměr: ")))
        print(f"Objem je {výpočet_objemu(těleso, strany)}")
        print(f"Povrch je {výpočet_povrchu(těleso, strany)}")
    else:
        print("Těleso není v seznamu")
        exit(1)


while True:
    main()
