def vstup_int(txt) -> int:
    while True:
        try:
            x: int = int(input(txt))
        except ValueError:
            print("Zadejte prosím číslo")
        else:
            return x


n: int = vstup_int("Zadejte n: ")
p: str = "* "
for i in range(n, 0, -1):
    print(p * i)
