import pylab as pl


def vstup_float_min_max(txt, min: float = None, max: float = None) -> float:  # type: ignore
    """Zadava cele cislo v zadanem rozsahu."""
    while True:
        try:
            cislo: float = float(input(txt))
            if min is not None and cislo < min:
                raise ValueError()
            if max is not None and cislo > max:
                raise ValueError()
            return cislo
        except ValueError:
            print(f"Zadej cislo v rozsahu {min} az {max}.")


hodnoty: list[float] = [
    vstup_float_min_max(f"""Zadej {"y" if j else "x"}{i}: """, 0)
    for i in range(1, 4)
    for j in range(0, 2)
]
x: list[float] = hodnoty[::2] + [hodnoty[0]]
y: list[float] = hodnoty[1::2] + [hodnoty[1]]
print(hodnoty)
print(x, y)
pl.plot(x, y, color="red")
pl.xlabel("x")
pl.ylabel("y")
pl.title("Trojuhelnik")
pl.xlim(0, max(x) + 1)
pl.ylim(0, max(y) + 1)

pl.show()
