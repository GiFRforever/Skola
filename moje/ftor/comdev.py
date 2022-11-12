import re
import math as mt
import os

prime_txt: str = "primes.txt"  # txt file with primes
prime_pickle: str = "primes.pickle"  # pickled primes
p_loaded: bool = False

try:  # Check if primes.txt and primes.pickle exists and are not empty
    if os.stat(prime_pickle).st_size == 0:
        if os.stat(prime_txt).st_size == 0:
            raise FileNotFoundError
        else:
            loading_type: str = "txt"
    else:
        loading_type: str = "pickle"
except:
    print("primes.txt/pickle neexistuje, vytvářím...")
    try:  # Check if wget is installed
        import wget
    except ModuleNotFoundError:
        import pip
        import subprocess
        import sys

        def install(package) -> None:
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])

        install("wget")
        import wget

        # Download temp.txt of primes
    wget.download("https://primes.utm.edu/lists/small/1000.txt", "temp.txt")
    # Make list of primes
    primes: list[int] = []
    with open("temp.txt", "r") as f:
        for line in f.readlines():
            try:
                primes.extend([int(i) for i in line.split()])
            except:
                pass
    p_loaded = True
    os.remove("temp.txt")
    # Make primes.txt
    with open(prime_txt, "w") as f:
        for p in primes:
            f.write(str(p) + "\n")
print("\nVložte celá čísla oddělená čárkami a získáte jejich dělitele.")

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


def input_cisla() -> list[int]:  # Input numbers
    while True:
        cisilka: list[int] = []
        try:
            vstup: str = input("Vstup: ")
            return [int(i) for i in re.findall(r"\b\d+\b", vstup)]
        except ValueError:
            if input == "q":
                exit()
            print("Neplatný vstup, zkuste zadat čísla oddělená čárkami.")
        except:
            print("Neznámá chyba, zadejte čísla oddělená čárkami.")


def delitele(cislo: int) -> list[int]:  # Get divisors of number
    pass
    return []
