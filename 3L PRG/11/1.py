def vstup_int() -> int:
    while True:
        try:
            return int(input("Zadejte číslo: "))
        except ValueError:
            print("Neplatné číslo, zadejte znovu")


# print triangle of stars with height n
def triangle(n: int) -> None:
    for i in range(n):
        print("* " * (i + 1))


triangle(vstup_int())
