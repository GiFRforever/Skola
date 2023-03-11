# 2
from random import randint

seznam: list[int] = [randint(1, 100) for _ in range(10)]
seznam.sort()
seznam2: list[int] = [x**2 for x in seznam]
l: int = len(str(seznam2[-1]))

print(" ".join([f"{x:>{l}}" for x in seznam]))
print(" ".join([f"{x:>{l}}" for x in seznam2]))

# 3
seznaml: list[int | str] = [x if x % 2 == 1 else " " * l for x in seznam2]
print(" ".join([f"{x:>{l}}" for x in seznaml]))

# 4
if c := seznam2.count(81):
    print(*["~" * l if x == 81 else " " * l for x in seznam2], sep=" ")
    print(f"Čílo 81 se vyskytuje {seznam2.count(81)}×.")
else:
    print("Čísla 81 se v seznamu nenacházejí.")

seznampepa: list[int | str] = [x if x != 81 else " " * l for x in seznam2]
print(" ".join([f"{x:>{l}}" for x in seznampepa]))
