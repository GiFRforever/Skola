from random import randint

čísla: list[int] = [randint(1, 100) for _ in range(20)]

print("Seznam čísel:")
print(*čísla, sep=", ")

sudá: list[int] = sorted([číslo for číslo in čísla if číslo % 2 == 0])
print("\nSudá čísla:")
print(*sudá, sep=", ")
print(f"Počet  sudých čísel: {len(sudá)}")
print(f"Součet sudých čísel: {sum(sudá)}")
print(f"Průměr sudých čísel: {sum(sudá) / len(sudá):.2f}")

lichá: list[int] = sorted([číslo for číslo in čísla if číslo % 2 == 1])
print("\nLichá čísla:")
print(*lichá, sep=", ")
print(f"Počet  lichých čísel: {len(lichá)}")
print(f"Součet lichých čísel: {sum(lichá)}")
print(f"Průměr lichých čísel: {sum(lichá) / len(lichá):.2f}")
