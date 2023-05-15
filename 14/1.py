import random

"""Házení kostkou."""
počet_hodů: int = int(input("Zadej počet hodů: "))
i: int = 0
suma: int = 0
while i < počet_hodů:
    hod: int = random.randint(1, 6)
    print(f"{i + 1}: kostka hodila {hod}")
    suma += hod
    i += 1
print(f"Průměrná hodnota hodu je {suma / počet_hodů}")
