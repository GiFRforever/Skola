from difflib import SequenceMatcher

ceníknávěsu = {
    # palety: Kč, typ návěsu
    18: (35, "návěs 6 tun"),
    28: (50, "návěs 24 tun"),
    33: (60, "MEGA návěs"),
}

ceníktarifu = {
    # tarif: násobič
    "standart": 1,
    "expres": 1.2,
}


def vstup_int(txt) -> int:
    while True:
        try:
            return int(input(txt))
        except ValueError:
            print("Neplatné číslo")


def similar(a, b) -> float:
    return SequenceMatcher(None, a, b).ratio()


def kalkulacka(km: int, palety: int, doprava: str) -> float:
    for palety_v_ceniku in ceníknávěsu.keys():
        if palety_v_ceniku >= palety:
            cena, typ = ceníknávěsu[palety_v_ceniku]
            break
    else:
        raise ValueError("Neplatný počet palet")

    for tarif in ceníktarifu.keys():
        # if similar(doprava, tarif) > 0.7:
        #     cena *= ceníktarifu[tarif]
        #     break
        if doprava == tarif:
            cena *= ceníktarifu[tarif]
            tarif = tarif
            break
    else:
        raise ValueError("Neplatný tarif")

    print("Pro přepravu je zvolen", typ, "s tarifem", tarif, "za cenu", cena, "Kč/km")
    return cena * km


km: int = vstup_int("Zadejte počet ujetých kilometrů: ")
palety: int = vstup_int("Zadejte počet přepravovaných palet: ")
while True:
    doprava = input("Zvolte dopravní možnost (standart/expres): ")
    for typ in ["standart", "expres"]:
        if similar(doprava, typ) > 0.7:
            doprava = typ
            break
    else:
        print("Neplatná možnost")
        continue
    break

print("Zaplatíte", round(kalkulacka(km, palety, doprava)), "Kč")
