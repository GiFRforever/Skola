def vstup_seznam(txt) -> list:
    while True:
        try:
            return input(txt).split()
        except ValueError:
            print("Neplatný vstup")

čísla = [int(x) for x in vstup_seznam("Zadejte čísla oddělená mezerou: ")]

print("Největší číslo je", max(čísla))
print("Nejmenší číslo je", min(čísla))
print("Průměr čísel je", sum(čísla) / len(čísla))
