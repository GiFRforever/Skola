def vstup(txt):
    bagr = None
    while bagr is None:
        try:
            bagr = int(input(txt))
            return bagr
        except:
            print("Vložte číslo!!")


delka = vstup("Zadejte délku v mm: ")
print(
    "{} mm = {} m + {} cm + {} mm".format(
        delka, delka // 1000, delka % 1000 // 10, delka % 10
    )
)
