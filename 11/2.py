from random import sample


def input_cisla() -> list[int]:  # Input numbers
    while True:
        try:
            vstup: str = input("Kolik čísel chcete vygenerovat? ")
            if vstup == "q":
                exit()
            kolik: int = int(vstup)
            if kolik < 1 or kolik > 100:
                raise ValueError

            cisla: list[int] = sample(range(1, 101), kolik)
            cisla.sort()
            return cisla
        except ValueError:
            print("Zadejte celé číslo větší než 0 a menší nebo rovno 100.")


def main() -> None:
    while True:
        cisla: list[int] = input_cisla()
        for c in cisla:
            print(f"{c}: 1 ", end="")
            for i in range(2, c):
                if c % i == 0:
                    print(i, end=" ")
            print(c)


main()
