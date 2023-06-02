from math import sqrt


def vstup_float(txt) -> float:
    while True:
        try:
            return float(input(txt))
        except ValueError:
            print("Zadejte prosím číslo.")


a: float = vstup_float("Zadejte stranu a: ")
b: float = vstup_float("Zadejte stranu b: ")
c: float = sqrt(a ** 2 + b ** 2)
print(f"Strana c má délku {c:.2f}")
