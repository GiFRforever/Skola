import cmath


def vstup(txt):
    bagr = None
    while bagr is None:
        try:
            bagr = float(input(txt))
            return bagr
        except:
            print("Vložte číslo!!")


a2 = 2 * vstup("Vložte a pro x^2: ")
b = vstup("Vložte b pro x: ")
c = vstup("Vložte c: ")
sD = cmath.sqrt(b ** 2 - 2 * a2 * c)
x1 = (-b + sD) / a2
x2 = (-b - sD) / a2
if round(x1.imag, 4) != 0:
    x1 = round(x1.real, 4) + round(x1.imag, 4) * 1j
else:
    x1 = round(x1.real, 4)
if round(x1.imag, 4) != 0:
    x2 = round(x2.real, 4) + round(x2.imag, 4) * 1j
else:
    x2 = round(x2.real, 4)
print("Kořeny rovnice jsou: x1 =", x1, " a x2 =", x2)
