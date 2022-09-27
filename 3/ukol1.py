import math


def vstup(txt):
    bagr = None
    while bagr is None:
        try:
            bagr = float(input(txt))
            return bagr
        except:
            print("Vložte číslo!!")


a = vstup("Zadejte stranu a: ")
b = vstup("Zadejte stranu b: ")
c = vstup("Zadejte stranu c: ")
if a + b < c or a + c < b or b + c < a:
    print("Trojúhelník nelze sestrojit")
else:
    s = (a + b + c) / 2
    print(
        "Trojúhelník o stranách délky {} cm, {} cm a {} cm má obvod {} cm a obsah {} cm2".format(
            round(a, 2),
            round(b, 2),
            round(c, 2),
            round(a + b + c, 2),
            round(math.sqrt(s * (s - a) * (s - b) * (s - c)), 2),
        )
    )
