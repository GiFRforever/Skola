vstup: str = input("Zadejte text: ")

while True:
    hledané: str = input("Zadejte hledané písmeno: ")
    if len(hledané) != 1:
        print("Musíte zadat právě jedno písmeno.")
        continue
    else:
        break

počet: int = vstup.count(hledané)
if počet == 0:
    print(f"""Písmeno "{hledané}" se v textu nevyskytuje.""")
else:
    print(f"""Písmeno "{hledané}" se v textu vyskytuje {počet}x.""")
