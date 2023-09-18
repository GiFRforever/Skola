tabulka: list[str] = [f"{d:>3} {hex(d)[2:].upper():0>2}   " for d in range(0, 256)]

for i in range(64):
    print(
        tabulka[:64][i],
        tabulka[64:128][i],
        tabulka[128:192][i],
        tabulka[192:][i],
        sep=" ",
    )
