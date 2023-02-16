import sys, os

arguments_set: set[str] = {
    r"%N",  # Název torrentu
    r"%L",  # Kategorie
    r"%G",  # Štítky (oddělené čárkou)
    r"%F",  # Umístění obsahu (stejné jako zdrojová cesta u vícesouborového torrentu)
    r"%R",  # Zdrojová cesta (první podadresář torrentu)
    r"%D",  # Cesta pro uložení
    r"%C",  # Počet souborů
    r"%Z",  # Velikost torrentu (v bytech)
    r"%T",  # Současný tracker
    r"%I",  # Info hash v1
    r"%J",  # Info hash v2
    r"%K",  # Torrent ID
}

print(sys.argv)

arguments: dict[str, str] = {
    argument: sys.argv[i][:-1] for i, argument in enumerate(arguments_set, start=1)
}

commands: list[str] = [
    """curl --form-string "message=%N download complete" "https://qbpushlite.fengmlo.com/api/v1/push/dDFTecZrCJQ4be7wlS9_g7YGbqW5CnmBIzH6X4DZdZLpTdbbqajseJHMPvEw24w5.VwCpJkayfQbRIDgrPIeT-yfKUFSJ0fW4""",
    # "python3 c:\\qlog\\autocatalog.py %D",
]

for c in commands:
    for aold, anew in arguments.items():
        c: str = c.replace(aold, anew)
    os.system(c)

with open("C:\\qlog\\qbittorrent.log", "w") as f:
    f.write(" | ".join([f"{aold}: {anew}" for aold, anew in arguments.items()]))
