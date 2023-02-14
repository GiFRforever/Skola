def vstup_float(txt) -> float:
    while True:
        try:
            return x if (x := float(input(txt))) > 0 else 0
        except ValueError:
            print("Neplatná hodnota, zadejte kladné reálné číslo.")


půjčka: float = vstup_float("Půjčka: ")
splátka: float = vstup_float("Měsíční splátka: ")
úrok: float = vstup_float("Úrok v %: ") / 100

n: int = 0
while půjčka > 0:
    if půjčka <= (np := půjčka + půjčka * úrok - splátka):
        print("Nelze splatit")
        break
    else:
        půjčka = np
        n += 1
        print(půjčka)
else:
    print("Splatíte za {} let a {} měsíců".format(*divmod(n, 12)))
    print(f"Celkem zaplatíte {n*splátka+půjčka:.2f} Kč")
