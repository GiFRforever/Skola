def vstup_int(txt) -> int:
    while True:
        try:
            x: int = int(input(txt))
        except ValueError:
            print("Zadejte prosím číslo")
        else:
            return x


n: int = vstup_int("Zadejte n: ")

for i in range(2, 21, 2):
    print(f"{i}^{n} = {i ** n}")
