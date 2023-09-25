from random import randint

DB = {}
DB["Mirek"] = ["Mirek", "Palackeho 16", "Olomouc", "732 675 810"]
DB["Dana"] = ["Dana", "Litovelska 7", "Olomouc", "775 321 405"]
DB["Jana"] = ["Jana", "Husova 7", "Litovel", "775 321 405"]
DB["Pepa"] = ["Pepa", "Komenskeho 9", "Praha", "845 207 536"]
DB["Marek"] = ["Marek", "Jarni", "Olomouc", "776 345 890"]
DB["Michal"] = ["Michal", "Mezice 20", "Mezice", "606 267 762"]
DB["Petra"] = ["Petra", "Neznama 34", "Olomouc", "731 456 789"]

i_jmeno = 0
i_ulice = 1
i_mesto = 2
i_telefon = 3

# DB[n] = [(n := input("Zadejte nové jméno: ")), input("Zadejte ulici a číslo popisné: "), input("Zadejte město: "), input("Zadejte telefonní číslo: ")]

print(
    "\nLidi z Olomouce:",
    *[
        f"{DB[n][i_jmeno]}, {DB[n][i_ulice]}, {DB[n][i_mesto]}, {DB[n][i_telefon]}"
        for n in DB
        if DB[n][i_mesto] == "Olomouc"
    ],
    sep="\n",
)

for n in DB:
    if DB[n][i_mesto] == "Olomouc":
        DB[n][i_mesto] = "Opava"

print(
    "\nVýpis všech (Ol -> Op):",
    *[
        f"{DB[n][i_jmeno]}, {DB[n][i_ulice]}, {DB[n][i_mesto]}, {DB[n][i_telefon]}"
        for n in DB
    ],
    sep="\n",
)

i_vek = 4

for n in DB:
    DB[n].append(str(randint(15, 25)))

print(
    "\nVýpis všech s věkem:",
    *[
        f"{DB[n][i_jmeno]}, {DB[n][i_ulice]}, {DB[n][i_mesto]}, {DB[n][i_telefon], DB[n][i_vek]}"
        for n in DB
    ],
    sep="\n",
)

print(
    "\nVýpis lidí s tel. na 7:",
    *[
        f"{DB[n][i_jmeno]}, {DB[n][i_ulice]}, {DB[n][i_mesto]}, {DB[n][i_telefon]}, {DB[n][i_vek]}"
        for n in DB
        if DB[n][i_telefon][0] == "7"
    ],
    sep="\n",
)
