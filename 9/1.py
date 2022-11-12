def vstup_int(txt):
    while True:
        try:
            cislo = int(input(txt))
            break
        except ValueError:
            print("Tohle není číslo!")
    return cislo
n = vstup_int("Zadej celé číslo: ")
for i in range(1,11):
    print(f"{i}*{n}= {i*n}")