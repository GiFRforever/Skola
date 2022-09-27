from math import *


def vstup(txt):
    bagr = None
    while bagr is None:
        try:
            bagr = int(input(txt))
            return bagr
        except:
            print("Vložte číslo!!")


a = vstup("Vložte číslo: ")
print(a, "! je ", round(factorial(a), 2))
