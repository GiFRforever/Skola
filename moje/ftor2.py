with open("primes.txt", "r") as f:
    primes = [int(p) for p in f]


def comd(num, den):
    for i in primes:
        if num % i == 0:
            if den % i == 0:
                return i
    return 0


def f_to_r(flt):
    if int(flt) == flt:
        return int(flt), 1
    flt_str = str(flt)
    flt_split = flt_str.split(".")
    num = int("".join(flt_split))
    den = 10 ** len(flt_split[1])
    devs = []
    while True:
        cdt = comd(num, den)
        if cdt != 0:
            num = num / cdt
            den = den / cdt
            devs.append(cdt)
        else:
            comdev = 1
            for i in devs:
                comdev = comdev * i
            return int(num), int(den), devs, comdev


from random import random

# a = random()
a = float(input())
print(a, f_to_r(a))