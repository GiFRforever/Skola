import re
import os
import multiprocessing as mp
import pickle
from time import sleep

if __name__ == "__main__":
    try:  # Check if tabulate is installed
        from tabulate import tabulate
    except ModuleNotFoundError:
        # print("module 'tabulate' is not installed")
        import pip
        import subprocess
        import sys

        def install(package) -> None:
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])

        # install("tabulate")
        from tabulate import tabulate

    try:  # Check if numpy is installed
        import numpy as np
    except ModuleNotFoundError:
        # print("module 'numpy' is not installed")
        import pip
        import subprocess
        import sys

        def install(package) -> None:
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])

        # install("numpy")
        import numpy as np
    jádra: int = mp.cpu_count()
    # jádra: int = 1


def init() -> None:

    prime_txt: str = "primes.txt"  # txt file with primes
    # jukni jestli tu je prime.txt, jestli ne, tak ho vytvoř a potom rozděl na pickle podle jader
    try:  # Check if primes.txt and primes.pickle exists and are not empty
        for i in range(jádra):
            if os.path.getsize(f"primes{i}.pickle") == 0:
                raise FileNotFoundError
        if os.path.isfile(f"primes{jádra+1}.pickle"):
            for file in os.listdir("./"):
                if file.endswith(".pickle") and file.startswith("primes"):
                    os.remove(file)
            raise FileNotFoundError
    except:
        if not os.path.isfile(prime_txt):
            print("primes.txt neexistuje, vytvářím...")
            try:  # Check if wget is installed
                import wget
            except ModuleNotFoundError:
                import pip
                import subprocess
                import sys

                def install(package) -> None:
                    subprocess.check_call(
                        [sys.executable, "-m", "pip", "install", package]
                    )

                install("wget")
                import wget

                # Download temp.txt of primes
            wget.download(
                "https://primes.utm.edu/lists/small/1000.txt", "tempprimes.txt"
            )
            # Make list of primes
            primes: list[int] = []
            with open("tempprimes.txt", "r") as f:
                for line in f.readlines():
                    try:
                        primes.extend([int(i) for i in line.split()])
                    except:
                        pass
            os.remove("tempprimes.txt")
            # Make primes.txt
            with open(prime_txt, "w") as f:
                for p in primes:
                    f.write(str(p) + "\n")
        else:
            print("primes.txt existuje, načítám...")
            with open(prime_txt, "r") as f:
                primes: list[int] = [int(i) for i in f.readlines()]
        # Make primes.pickle
        délka: int = len(primes)
        for i in range(jádra):
            with open(f"primes{i}.pickle", "wb") as f:
                pickle.dump(primes[i::jádra], f)
    print("\nVložte celá čísla oddělená čárkami a zjistěte, zda jsou prvočísla.")

    # init of processes
    for i in range(jádra):
        globals()[f"pipe_p_{i}"], globals()[f"pipe_c_{i}"] = mp.Pipe()
        globals()[f"prcs{i}"] = mp.Process(
            target=delitele, args=(i, globals()[f"pipe_c_{i}"])
        )
        globals()[f"prcs{i}"].start()
    sleep(1)
    print(f"Počet jáder: {jádra}      ", end="\r")
    sleep(1)
    print("Loading...           ", end="\r")
    for i in range(jádra):
        print(globals()[f"pipe_p_{i}"].recv(), end="\r")
    print("Loaded.              ", end="\r")


def input_cisla() -> list[int]:  # Input numbers
    while True:
        cisla: list[int] = []
        vstup: str = input("Vstup: ")
        try:
            cisla = [int(i) for i in re.findall(r"\b\d+\b", vstup)]
            if cisla == []:
                raise Exception
            return cisla
        except:
            if vstup == "q":
                for i in range(jádra):
                    globals()[f"prcs{i}"].terminate()
                exit()
            print("Neplatný vstup, zkuste zadat čísla oddělená čárkami.")


def delitele(proc: int, conn) -> None:  # Get divisors of number
    import pickle

    with open(f"primes{proc}.pickle", "rb") as f:
        primes: list[int] = pickle.load(f)
        # print(primes)
    conn.send(f"Loaded {proc}")
    # cislo: int = 0
    # print(f"Process {proc} started.")
    while (cislo := conn.recv()) != 0:  # špatně!!!
        # print(f"Process {proc} received {cislo}.")
        temp: list[int] = []
        n: int = 0
        while n == 0:
            m: int = 0
            for p in primes:
                if cislo % p == 0:
                    cislo //= p
                    temp.append(p)
                    m: int = 1
            if m == 0:
                n = 1
        # print(temp)
        conn.send(temp)
        cislo = 0


def main() -> None:
    init()
    while True:
        cisla: list[int] = input_cisla()
        c_0: list[int] = []
        # process transfer
        for c, i in zip(cisla, range(len(cisla))):
            # Send numbers to processes
            for j in range(jádra):
                globals()[f"pipe_p_{j}"].send(c)
            # Receive divisors from processes
            globals()[f"c_{i}"] = []
            for j in range(jádra):
                globals()[f"c_{i}"].extend(globals()[f"pipe_p_{j}"].recv())

        # je prvočíslo?
        for i in range(len(cisla)):
            if len(globals()[f"c_{i}"]) <= 1:
                print(f"Číslo {cisla[i]} je prvočíslo.")
            else:
                print(
                    f"{cisla[i]} není prvočíslo. Dělitelé jsou:",
                    end=" ",
                )
                globals()[f"c_{i}"].sort()
                temporrary: list[int] = []
                stary: int = 0
                for j in globals()[f"c_{i}"]:
                    if j != stary:
                        kolik = globals()[f"c_{i}"].count(j)
                        for k in range(0, kolik + 1):
                            temporrary.append(j ** k)
                        stary = j
                temporrary.sort()
                print(*temporrary, sep=", ")
        # temporary logging
        """for i in range(len(cisla)):
            print(f"Dělitele čísla {cisla[i]}: {globals()[f'c_{i}']}")"""
        # process divisors
        """
        comdevs: list[int] = globals()["c_0"]
        if len(cisla) != 1:
            for i in range(1, len(cisla)):
                temp: list[int] = []
                temp2: list[int] = (globals()[f"c_{i}"]).copy()
                for j, k in zip(comdevs, range(len(comdevs))):
                    for l, m in zip(temp2, range(len(temp2))):
                        if j == l:
                            temp.append(j)
                            del temp2[m]
                            break
                comdevs = temp
        # print(comdevs)
        cisilkaout: list = []
        # print(cisla)
        for c, i in zip(cisla, range(len(cisla))):
            globals()[f"c_{i}"].sort()
            globals()[f"ct_{i}"] = " ".join(str(x) for x in globals()[f"c_{i}"])
            cisilkaout.append([c, c / np.prod(comdevs), globals()[f"ct_{i}"]])
        if comdevs != []:
            print(tabulate(cisilkaout, headers=["in", "out", "devs"]))
            print(f"Společní jmenovatelé: {comdevs} = {np.prod(comdevs)}")
        else:
            print("Žádný společný jmenovatel")"""


if __name__ == "__main__":
    main()
