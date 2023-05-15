primes: list[str] = []
for m in range(1, 51, 1):
    with open(f"moje/p/primes{m}.txt", "r") as f:
        alllines: list[str] = f.readlines()
        alllines.remove(alllines[0])
        alllines.remove(alllines[0])
        for l in alllines:
            line: list[str] = l.split(" ")
            for n in line:
                if n.isdigit():
                    primes.append(n)
    print(f"primes{m}.txt loaded")
with open("moje/p/primes.txt", "w") as f:
    for p in primes:
        f.write(f"{p}\n")
    print("primes.txt saved")

with open("moje/p/primes_desc.txt", "w") as f:
    for p in reversed(primes):
        f.write(f"{p}\n")
    print("primes_desc.txt saved")
