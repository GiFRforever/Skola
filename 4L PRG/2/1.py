import sys
vstup: str = input("Zadejte čísla oddělená mezerou: ")
cisla: list[int] = [int(x) for x in vstup.split()]
print(*set(cisla))