from typing_extensions import Literal


with open("moje/primes.txt", "r") as f:
    primes: list[int] = [int(p) for p in f]

"""
def comd(num, den) -> int:
    for i in primes:
        if num % i == 0:
            if den % i == 0:
                return i
    return 0
"""


def f_to_r(flt) -> tuple[int, int] | tuple[int, int, list[int], int]:
    if int(flt) == flt:
        return int(flt), 1
    flt_str: str = str(flt)
    flt_split: list[str] = flt_str.split(".")
    num: int | float = int("".join(flt_split))
    den: int | float = 10 ** len(flt_split[1])
    devs: list[int] = []
    while True:
        # cdt: int = comd(num, den)
        cdt: int = 1
        while cdt != 0:
            cdt: int = 0
            for i in primes:
                if num % i == 0:
                    if den % i == 0:
                        cdt: int = i
            if cdt != 0:
                num = num / cdt
                den = den / cdt
                devs.append(cdt)
        comdev: int = 1
        for i in devs:
            comdev = comdev * i
        return int(num), int(den), devs, comdev


from random import random
from time import time


# a: float = float(input())
t1: float = time()
for i in range(0, 1000, 1):
    a: float = random()
    f_to_r(a)
    # print(a, f_to_r(a))
t2: float = time()
print((t2 - t1) / 1000)
