cislo = 125
primes: list[int] = [2,3,5,7,11,13,17,19]
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
print(temp)