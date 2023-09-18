from random import randint

cisla: list[list[str]] = [
    ["|       |", "|   *   |", "|       |"],
    ["|*      |", "|       |", "|      *|"],
    ["|*      |", "|   *   |", "|      *|"],
    ["|*     *|", "|       |", "|*     *|"],
    ["|*     *|", "|   *   |", "|*     *|"],
    ["|*     *|", "|*     *|", "|*     *|"],
]

pocet_hodu: int = int(input("Zadej pocet hodu: "))

hody: list[int] = []


def vypis_hod(cislo: int) -> None:
    for radek in cisla[cislo - 1]:
        print(radek)


for i in range(pocet_hodu):
    ktery: int = randint(1, 6)
    hody.append(ktery)
    print(f"{i}. hod: {ktery}")
    vypis_hod(ktery)

print(f"Průmerná hodnota: {sum(hody) / pocet_hodu:.2f}")
