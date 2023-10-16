from random import randint
with open("vstup.txt", "w+") as vstup, open("vystup.txt", "w") as vystup:
    for _ in range(100):
        vstup.write(f"{randint(10, 99)} {randint(10, 99)}\n")
    
    vstup.seek(0)
    for line in vstup:
        cislo1, cislo2 = line.split()
        vystup.write(f"{cislo1}+{cislo2}={int(cislo1) + int(cislo2)}\n")