def vstup_int(txt):
    while True:
        try:
            return int(input(txt))
        except:
            print("Zadejte celé číslo!")

n = vstup_int("Zadej celé číslo: ")
print(int(n*(n+1)/2))
