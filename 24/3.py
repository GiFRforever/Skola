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


# Nacti data
min: float = vstup_float_min_max("Zadej spodní hranici x: ")
max: float = vstup_float_min_max("Zadej horní hranici x: ", min)

x = pl.linspace(min, max, 20)
y = 2 / (x + 1)

pl.plot(x, y, color="red")
pl.xlabel("x")
pl.ylabel("y")
pl.title("Graf funkce y = 2/(x+1)")
pl.show()
