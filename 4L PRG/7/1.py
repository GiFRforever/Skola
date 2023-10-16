try:
    with open("pokus.txt", "r") as pokus, open("kopie.txt", "w") as kopie:
            for line in pokus:
                kopie.write(line)
except FileNotFoundError:
     print("Soubor neexistuje.")