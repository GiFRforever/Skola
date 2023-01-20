import os

prime_txt: str = "primes.txt"  # txt file with primes
if not os.path.isfile(prime_txt):
    print("primes.txt neexistuje, vytvářím...", end="\r")
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
    wget.download("https://primes.utm.edu/lists/small/100000.txt", "tempprimes.txt")
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
    print("primes.txt existuje, načítám...", end="\r")
    with open(prime_txt, "r") as f:
        primes: list[int] = [int(i) for i in f.readlines()]

print("Zadejte číslo, program vám vypíše prvočísla do dané hodnoty.")

# print(primes)
# print(len(primes))

while True:
    cisilko: int = int(input("Zadej číslo: "))
    if cisilko > 1299827:
        Exception("Ochrana počítače před přetížením")
    print("Prvočísla do", cisilko, "jsou:")
    for i in primes:
        if i > cisilko:
            break
        print(i, end=" ")
    print()
