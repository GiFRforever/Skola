print("Formát: cena, gramy např.: 42.9,200")
tc, tg = eval(input("Zadejte cenu a gramáš másla v Teslu: "))
gc, gg = eval(input("Zadejte cenu a gramáž másla v Globusu: "))
lc, lg = eval(input("Zadejte cenu a gramáž másla v Lidl: "))
# nejdražší
if tc / tg > gc / gg and tc / tg > lc / lg:
    print("Nejdražší máslo má Tesco")
elif gc / gg > tc / tg and gc / gg > lc / lg:
    print("Nejdražší máslo má Globus")
elif lc / lg > tc / tg and lc / lg > gc / gg:
    print("Nejdražší máslo má Lidl")
# nejlevnější
if tc / tg < gc / gg and tc / tg < lc / lg:
    print("Nejlevnější máslo má Tesco")
elif gc / gg < tc / tg and gc / gg < lc / lg:
    print("Nejlevnější máslo má Globus")
elif lc / lg < tc / tg and lc / lg < gc / gg:
    print("Nejlevnější máslo má Lidl")
# o kolik % je dražší nejdražší než nejlevnější
if tc / tg > gc / gg and tc / tg > lc / lg:
    if gc / gg > lc / lg:
        print(
            f"Másla v Teslu je o {int(round((tc / tg - lc / lg) / (lc / lg) * 100, 0))} % dražší než másla v Lidl."
        )
    else:
        print(
            f"Másla v Teslu je o {int(round((tc / tg - gc / gg) / (gc / gg) * 100, 0))} % dražší než másla v Globusu."
        )
elif gc / gg > tc / tg and gc / gg > lc / lg:
    if tc / tg > lc / lg:
        print(
            f"Másla v Globusu je o {int(round((gc / gg - lc / lg) / (lc / lg) * 100, 0))} % dražší než másla v Lidl."
        )
    else:
        print(
            f"Másla v Globusu je o {int(round((gc / gg - tc / tg) / (tc / tg) * 100, 0))} % dražší než másla v Teslu."
        )
elif lc / lg > tc / tg and lc / lg > gc / gg:
    if tc / tg > gc / gg:
        print(
            f"Másla v Lidl je o {int(round((lc / lg - gc / gg) / (gc / gg) * 100, 0))} % dražší než másla v Globusu."
        )
    else:
        print(
            f"Másla v Lidl je o {int(round((lc / lg - tc / tg) / (tc / tg) * 100, 0))} % dražší než másla v Teslu."
        )
