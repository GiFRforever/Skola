import re
import math as mt
import os

prime_txt = "primes.txt"
try:
    with open(prime_txt, "r") as f:
        pass
except:
    print("primes.txt neexistuje, vytvářím...")
    try:
        import wget
    except ModuleNotFoundError:
        import pip
        import subprocess
        import sys

        def install(package):
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])

        install("wget")
        import wget
    wget.download("https://primes.utm.edu/lists/small/1000.txt", "temp.txt")
    primes = []
    with open("temp.txt", "r") as f:
        for line in f.readlines():
            try:
                primes.extend([int(i) for i in line.split()])
            except:
                pass
    os.remove("temp.txt")
    # print(primes)
    with open(prime_txt, "w") as f:
        for p in primes:
            f.write(str(p) + "\n")
print("\nVložte celá čísla oddělená čárkami a získáte jejich dělitele.")

try:
    from tabulate import tabulate
except ModuleNotFoundError:
    # print("module 'tabulate' is not installed")
    import pip
    import subprocess
    import sys

    def install(package):
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

    # install("tabulate")
    from tabulate import tabulate
try:
    import numpy as np
except ModuleNotFoundError:
    # print("module 'numpy' is not installed")
    import pip
    import subprocess
    import sys

    def install(package):
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

    # install("numpy")
    import numpy as np

while True:
    vstup = None
    cisilka: list = []
    c_0: list = []
    while vstup == None:
        vstup = input("Vložte list: ")
        if vstup == "q":
            os.remove(prime_txt)
            exit()
        try:
            vstup = re.findall(r"\b\d+\b", vstup)
            if vstup == []:
                raise Exception
            cisilka = [int(x) for x in vstup]
        except:
            print("Chybný vstup!")
            vstup = None
    with open(prime_txt, "r") as f:
        primes = []
        for line in f:
            if int(line) <= (min(cisilka)):
                primes.append(int(line))
            else:
                break
    for i, c in zip(range(len(cisilka)), cisilka):
        temp: list[int] = []
        n: int = 0
        while n == 0:
            m: int = 0
            for x in primes:
                if c % x == 0:
                    c /= x
                    temp.append(x)
                    m: int = 1
            if m == 0:
                n = 1
        globals()[f"c_{i}"] = temp
    comdevs: list[int] = c_0
    if len(cisilka) != 1:
        for i in range(1, len(cisilka)):
            temp: list[int] = []
            temp2: list[int] = (globals()[f"c_{i}"]).copy()
            for j, k in zip(comdevs, range(len(comdevs))):
                for l, m in zip(temp2, range(len(temp2))):
                    if j == l:
                        temp.append(j)
                        del temp2[m]
                        break
            comdevs = temp
    cisilkaout: list = []
    print(cisilka)
    for c, i in zip(cisilka, range(len(cisilka))):
        globals()[f"c_{i}"].sort()
        globals()[f"ct_{i}"] = " ".join(str(x) for x in globals()[f"c_{i}"])
        cisilkaout.append([c, c / np.prod(comdevs), globals()[f"ct_{i}"]])
    if comdevs != []:
        print(tabulate(cisilkaout, headers=["in", "out", "devs"]))
        print(f"Společní jmenovatelé: {comdevs} = {np.prod(comdevs)}")
    else:
        print("Žádný společný jmenovatel")
