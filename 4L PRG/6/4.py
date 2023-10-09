def vstup_seznam(txt) -> list:
    while True:
        try:
            return input(txt).split()
        except ValueError:
            print("Neplatný vstup")


seznam = vstup_seznam("Zadejte slova oddělená mezerou: ")
for slovo in seznam:
    for písmeno in slovo:
        if písmeno not in "aeiouyAEIOUYáéíóúýÁÉÍÓÚÝěĚúÚůŮ":
            print(písmeno, end="")
    print()
