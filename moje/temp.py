import random


with open("moje/p/primes.txt", "r") as f:
    primes: list[int] = [int(f.readline()) for i in range(10)]
# generate 10 random numbers in list
flt = [random.randint(2, 1000000) for i in range(10)]
out: list[int] = []
m=0
n=0
while n == 0:
    while m == 0:
        for i in primes:
            for int in flt:
                if int % i == 0:
                    out.append(i)
                    num //= i
                    den //= i
                    m:int = 1
                    break
        if m == 1:
            m = 0
            continue
        n = 1
        break

print(out)
print(f"{flt} = {num}/{den}")