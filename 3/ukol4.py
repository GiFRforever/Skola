import math


def vstup(txt):
    bagr = None
    while bagr is None:
        try:
            bagr = float(input(txt))
            return bagr
        except:
            print("Vložte číslo!!")


přepona = vstup("Zadejte délku přepony: ")
odvěsna = vstup("Zadejte délku odvěsny: ")
# Vypočítáme délku druhé odvěsny pomocí Pythagorovy věty
# a^2 + b^2 = c^2   =>   b^2 = c^2 - a^2    =>   b = sqrt(c^2 - a^2)    =>   b = sqrt(c^2) - sqrt(a^2)
odvěsna2 = math.sqrt(přepona**2 - odvěsna**2)
print("Délka druhé odvěsny je {} cm".format(round(odvěsna2, 2)))
