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
print(
    "Objem a povrch kvádru o stranách délky {} cm, {} cm a {} cm je {} cm³ a {} cm²".format(
        round(a, 2),
        round(b, 2),
        round(c, 2),
        round(a * b * c, 2),
        round(2 * (a * b + b * c + a * c), 2),
    )
)
