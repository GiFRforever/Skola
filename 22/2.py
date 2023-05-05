def vstup_float(txt: str) -> float:
    while True:
        try:
            return float(input(txt))
        except ValueError:
            print("Zadejte prosím číslo.")


def vstup_int(txt: str) -> int:
    while True:
        try:
            return int(input(txt))
        except ValueError:
            print("Zadejte prosím celé číslo.")


prvocisla: list[int] = [2, 3, 5, 7, 11, 13, 17, 19, 23]


def exp(base, power) -> float:
    for prv in prvocisla:
        if power % prv == 0:
            return exp(base**prv, power / prv)
    return base**power


základ: float = vstup_float("Zadejte základ: ")
mocnina: int = vstup_int("Zadejte mocninu: ")
print(f"{základ}^{mocnina} = {exp(základ, mocnina)}")
