def vstup_int(txt) -> int:
    while True:
        try:
            return x if (x := int(input(txt))) > 4 else 4
        except ValueError:
            print("Neplatná hodnota, zadejte přirozené číslo.")


n: int = vstup_int("Max druhá mocnina: ")

x: int = 2
while (p := x ** 2) < n:
    print(f"{x}^2 = {p}")
    x += 2
