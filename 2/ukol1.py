from math import *


def vstup(txt):
    bagr = None
    while bagr is None:
        try:
            bagr = int(input(txt))
            return bagr
        except:
            print("Vložte číslo!!")


r = vstup("Vložte poloměr koule: ")
print(
    "Pro kouly s r = ",
    r,
    " je objem ",
    round(4 * pi * (r ** 2), 2),
    " a povrch ",
    round(4 / 3 * pi * (r ** 3), 2),
)
