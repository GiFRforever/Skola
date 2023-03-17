text: str = input("Zadejte text: ")
samohlasky: dict[str, int] = {
    "a": 0,
    "e": 0,
    "i": 0,
    "o": 0,
    "u": 0,
    "y": 0,
    "á": 0,
    "é": 0,
    "í": 0,
    "ó": 0,
    "ú": 0,
    "ý": 0,
}

for znak in text.lower():
    if znak in samohlasky:
        samohlasky[znak] += 1

for znak, pocet in samohlasky.items():
    if pocet != 0:
        print(f"{znak}: {pocet}")
