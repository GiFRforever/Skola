primes: list[int] = [2]

start = int(input("Zadejte začátek: "))
end = int(input("Zadejte konec: "))

n = 3
for _ in range(int(end/2)):
    for prime in primes:
        if n % prime == 0:
            break
    else:
        primes.append(n)
    n += 2

print(*(x for x in primes if x >= start))