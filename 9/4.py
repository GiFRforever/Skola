def vstup_int(txt):
    while True:
        try:
            return int(input(txt))
        except:
            print("Zadejte celé číslo!")

a = vstup_int("Zadej spodní hranici intervalu: ")
b = vstup_int("Zadej horní hranici intervalu: ")
if a > b:
    print("\033[91mNapsali jste je opačně!\033[0m")
    a, b = b, a
out = []
for i in range(a, b+1):
    if i % 3 == 0:
        out.append(i)
if out == []:
    print(f"V intervalu ({a},{b}) nejsou žádná čísla dělitelná třemi.")
elif len(out) == 1:
    print(f"V intervalu ({a},{b}) je jedno číslo dělitelné třemi: {out[0]}")
else:
    print(f"V intervalu ({a},{b}) jsou tato čísla dělitelná třemi: {', '.join(map(str, out))}")
