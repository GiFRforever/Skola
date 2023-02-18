import sys, os
from time import sleep

arguments_list: list[str] = [
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
]

arguments: dict[str, str] = {
    argument: sys.argv[i][:-1] for i, argument in enumerate(arguments_list, start=1)
}

with open("C:\\qlog\\qbittorrent.log", "w") as f:
    f.write(" | ".join([f"{aold}: {anew}" for aold, anew in arguments.items()]))

commands: list[str] = [
    """curl --form-string "message=%N download complete" "https://qbpushlite.fengmlo.com/api/v1/push/9Dtv9oC6o2O32ayy22847JbDqoPjViNiHgFO841_hdgmkE1Zg36Jgw-NNygvGnFc.6johBQ3FJruRSeHrWBGxb5lOnavMTFI-""",
    # r'python3 c:\\qlog\\autocatalog.py "%F" %G', # this is for moving files (now deprecated)
    r'python3 c:\\qlog\\autocatalog2.py "%F" %G',
]

sleep(int(arguments["%Z"]) / (1048576 * 50))

try:
    for c in commands:
        for aold, anew in arguments.items():
            c: str = c.replace(aold, anew)
        os.system(c)
    else:
        done = "Přesunutí úspěšné"
except Exception:
    done = "ERROR - Přesunutí neúspěšné"
with open("C:\\qlog\\qbittorrent.log", "a") as f:
    f.write(done)

sleep(5)
