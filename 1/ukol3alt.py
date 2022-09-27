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

vstup = input("Vložte řetězec:")
cisla = []
out = []
for z in vstup.split():
    if z.isdigit():
        cisla.append(z)

for i in cisla:
    try:
        pos = i[-1]
    except:
        pos = "Není"
    try:
        ppos = i[-2]
    except:
        ppos = "Není"
    out.extend([[i, pos, ppos]])
print(tabulate(out, headers=["Číslo", "Poslední", "Předposlední"]))
