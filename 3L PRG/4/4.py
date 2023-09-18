try:
    from tabulate import tabulate

    # print("module 'tabulate'' is installed")
except ModuleNotFoundError:
    print("module 'tabulate' is not installed")
    import pip
    import subprocess
    import sys

    def install(package):
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

    install("tabulate")
    from tabulate import tabulate


def vstup_f(txt):
    """Vstupní funkce"""
    while True:
        try:
            vsthod = float(input(txt))
            return vsthod
        except ValueError:
            print("Neplatná hodnota")


plán_třžby_čtvr = vstup_f("Zadejte roční plán tržeb: ") / 4
čtvrt1 = vstup_f("Zadejte výši tržeb za první čtvrtletí: ")
čtvrt2 = vstup_f("Zadejte výši tržeb za druhé čtvrtletí: ")
čtvrt3 = vstup_f("Zadejte výši tržeb za třetí čtvrtletí: ")
čtvrt4 = vstup_f("Zadejte výši tržeb za čtvrté čtvrtletí: ")

out = []
for i, n in zip([čtvrt1, čtvrt2, čtvrt3, čtvrt4], range(1, 5)):
    out.extend([[n, plán_třžby_čtvr, i, int(i / plán_třžby_čtvr * 100)]])

print(tabulate(out, headers=["Čtvrtletí", "Plán", "Skutečnost", "Plnění v %"]))
