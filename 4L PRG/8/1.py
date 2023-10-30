with open("text.txt", "r") as f:
    text = f.read()

pismena = {}
ostatni = {}
for pismeno in text:
    if pismeno.isalpha():
        if pismeno in pismena:
            pismena[pismeno] += 1
        else:
            pismena[pismeno] = 1
    else:
        if pismeno in ostatni:
            ostatni[pismeno] += 1
        else:
            ostatni[pismeno] = 1

if "\n" in ostatni:
    ostatni["\\n"] = ostatni.pop("\n")


print("Pismena:", len(pismena))
for key, value in sorted(pismena.items()):
    print(f"'{key}': {value}")

print("Ostatni:", len(ostatni))
for key, value in sorted(ostatni.items()):
    print(f"'{key}': {value}")
