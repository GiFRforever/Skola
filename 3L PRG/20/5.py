print(
    f"""Řetězce {"" if (sorted([ord(i) for i in input("Zadejte první řetězec: ")]) == sorted([ord(j) for j in input("Zadejte druhý řetězec: ")])) else "ne" }jsou anagramy."""
)
