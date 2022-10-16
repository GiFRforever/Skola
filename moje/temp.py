with open("moje/p/primes.txt", "r") as f:
    data: str = f.read()
    for x in range(1,10):
        globals()["primes_list_" + str(x)] = [int(i) for i in data.split("\n") if len(i) == x]
    print("Primes loaded.")

for x in range(1,10):
    with open(f"moje/p/primes{x}.txt", "w") as f:
        for p in globals()["primes_list_" + str(x)]:
            f.write(f"{p}\n")
        print(f"primes{x}.txt saved")