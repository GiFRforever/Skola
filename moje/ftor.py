def float_to_ratio(flt):
    if int(flt) == flt:  # to prevent 3.0 -> 30/10
        return int(flt), 1
    flt_str = str(flt)
    flt_split = flt_str.split(".")
    numerator = int("".join(flt_split))
    denominator = 10 ** len(flt_split[1])
    return numerator, denominator, numerator / denominator


def f_r(flt) -> int | tuple[int, int, float, float]:
    if int(flt) == flt:
        return int(flt)
    flt_str: str = str(flt)
    flt_split: list[str] = flt_str.split(".")
    numerator: int = int("".join(flt_split))
    denominator: int = 10 ** len(flt_split[1])
    dev: float = 1
    for i in range(2, 10001, 1):
        i: float = i / 10
        zbn: float = numerator % i
        if zbn > 1 or zbn < -1:
            pass
        else:
            zbd: float = denominator % i
            if zbd > 1 or zbd < -1:
                pass
            else:
                dev: float = i
    return (
        int(numerator // dev),
        int(denominator // dev),
        float(dev),
        float((numerator / dev) / (denominator / dev)),
    )


def f_r3(flt, rep=100001) -> tuple[int, int, float, float]:
    h:tuple[int, int] = flt.as_integer_ratio()
    numerator: int = h[0]
    denominator: int = h[1]
    dev:float = 1
    for i in range(2, rep, 1):
        zbn: int = numerator % i
        if zbn > 1 or zbn < -1:
            pass
        else:
            zbd = denominator % i
            if zbd > 1 or zbd < -1:
                pass
            else:
                dev = i
    return (
        numerator // dev,
        denominator // dev,
        dev,
        (numerator / dev) / (denominator / dev),
    )


def f_r2(flt:float, prc=0, rep=100000) -> tuple[int, int, float]:
    # print(flt,prc,rep)
    num:int = 1
    den:int = 1
    rat: float = num / den
    if prc != 0 and prc != -1:
        flt = round(flt, prc)
    elif prc == 0:
		# repetitive calculation
        if flt > 0:
            for i in range(0, rep):
                while rat > flt:
                    den += 1
                    rat = num / den
                while rat < flt:
                    num += 1
                    rat = num / den
                # print(rat)
        else:
            for i in range(0, rep):
                while rat < flt:
                    den += 1
                    rat = num / den
                while rat > flt:
                    num -= 1
                    rat = num / den
                # print(rat)
        return num, den, rat
	# precision calculation
    if flt > 0:
        while rat != flt:
            while rat > flt:
                den += 1
                rat = num / den
            while rat < flt:
                num += 1
                rat = num / den
            # print(rat)
    else:
        while rat != flt:
            while rat < flt:
                den += 1
                rat = num / den
            while rat > flt:
                num -= 1
                rat = num / den
            # print(rat)
    return num, den, rat

with open("moje/primes.txt", "r") as f:
    primes: list[int] = [int(p) for p in f]


def comd(num, den) -> int:
    for i in primes:
        if num % i == 0:
            if den % i == 0:
                return i
    return 0


def f_to_r(flt) -> tuple[int,int]|tuple[int, int, list[int], int]:
    if int(flt) == flt:
        return int(flt), 1
    flt_str: str = str(flt)
    flt_split: list[str] = flt_str.split(".")
    num: int = int("".join(flt_split))
    den: int = 10 ** len(flt_split[1])
    devs: list[int] = []
    while True:
        cdt: int = comd(num, den)
        if cdt != 0:
            num = num // cdt
            den = den // cdt
            devs.append(cdt)
        else:
            comdev: int = 1
            for i in devs:
                comdev = comdev * i
            return int(num), int(den), devs, comdev

def f_to_r2(flt) -> tuple[int, int]|tuple[int, int, list[int], int]:
    if int(flt) == flt:
        return int(flt), 1
    flt_str: str = str(flt)
    flt_split: list[str] = flt_str.split(".")
    num: int|float = int("".join(flt_split))
    den: int|float = 10 ** len(flt_split[1])
    devs: list[int] = []
    while True:
        #cdt: int = comd(num, den)
        cdt: int = 1
        while cdt != 0:
            cdt: int = 0
            for i in primes:
                if num % i == 0:
                    if den % i == 0:
                        cdt: int =  i
            if cdt != 0:
                num = num / cdt
                den = den / cdt
                devs.append(cdt)
        comdev: int = 1
        for i in devs:
            comdev = comdev * i
        return int(num), int(den), devs, comdev
"""
from fractions import fraction
def fraction_to_r(flt):
	return fraction(flt), fraction(flt).limit_denominator()
	"""
from time import time, sleep
from random import random

# a = random()
def vstup(txt):
    vs = input(txt)
    if vs == "" or int(vs) <= 0:
        return 0
    else:
        return int(vs)


c: list[float|int] = []
c.append(float(input("flt:")))
#c.append(random())
p: int = vstup("prc [def: 0 -> rep, -1 -> precise]: ")
r: int = vstup("rep [def: 100000]: ")
if p == 0:
    c.append(0)
else:
    c.append(p)
if r == 0:
    c.append(100000)
else:
    c.append(r)
a: float = c[0]
print(c)
sleep(1)
t1: float = time()
b: tuple[int, int] = a.as_integer_ratio()
t2: float = time()
print("a.i.r",b, b[0] / b[1])
t3: float = time()
print("f.t.r",float_to_ratio(a))
t4: float = time()
print("f.r",f_r(a)) # nice
t5: float = time()
print("f.r2",f_r2(flt=c[0], prc=int(c[1]), rep=int(c[2])))
t6: float = time()
print("f.r3",f_r3(c[0], int(c[2])))
t7: float = time()
print("f.t.r2",f_to_r(a))
t8: float = time()
print("f.t.r3",f_to_r2(a)) # long but nice
t9: float = time()
print(t2 - t1, t4 - t3, t5 - t4, t6 - t5, t7 - t6, t8 - t7, t9 - t8)
