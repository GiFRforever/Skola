def vstup_f(txt):
    """Vstupní funkce"""
    while True:
        try:
            vsthod = float(input(txt))
            return vsthod
        except ValueError:
            print("Neplatná hodnota")


minut = vstup_f("Zadejte počet minut: ")
týdny = minut // 10080
dny = (minut % 10080) // 1440
hodiny = ((minut % 10080) % 1440) // 60
minuty = ((minut % 10080) % 1440) % 60
print("Týdnů: {}".format(int(týdny)))
print("Dní:   {}".format(int(dny)))
print("Hodin: {}".format(int(hodiny)))
print("Minut: {}".format(int(minuty)))
