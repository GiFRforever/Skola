"""with open("moje/p/primes.txt", "r") as f:
    primes = [int(f.readline()) for i in range(10)]
flt = 0.0225
flt_split: list[str] = str(flt).split(".")
num: int = int("".join(flt_split))
den: int = 10 ** len(flt_split[1])
out: list[int] = []
m=0
n=0
while n == 0:
    while m == 0:
        for i in primes: # type: ignore
            if num % i == 0:
                if den % i == 0:
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
print(f"{flt} = {num}/{den}")"""

