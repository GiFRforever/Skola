def float_to_ratio(flt):
    if int(flt) == flt:  # to prevent 3.0 -> 30/10
        return int(flt), 1
    flt_str = str(flt)
    flt_split = flt_str.split(".")
    numerator = int("".join(flt_split))
    denominator = 10 ** len(flt_split[1])
    return numerator, denominator, numerator / denominator


def f_r(flt):
    if int(flt) == flt:
        return int(flt)
    flt_str = str(flt)
    flt_split = flt_str.split(".")
    numerator = int("".join(flt_split))
    denominator = 10 ** len(flt_split[1])
    for i in range(2, 10001, 1):
        i = i / 10
        zbn = numerator % i
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


def f_r3(flt, rep=100001):
    h = flt.as_integer_ratio()
    numerator = h[0]
    denominator = h[1]
    for i in range(2, rep, 1):
        zbn = numerator % i
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


def f_r2(flt, prc=0, rep=100000):
    # print(flt,prc,rep)
    num = 1
    den = 1
    rat = num / den
    if prc != 0:
        flt = round(flt, prc)
    else:
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


c = []
c.append(float(input("flt:")))
p = vstup("prc:")
r = vstup("rep:")
if p == 0:
    c.append(0)
else:
    c.append(p)
if r == 0:
    c.append(100000)
else:
    c.append(r)
a = c[0]
print(c)
sleep(1)
t1 = time()
b = a.as_integer_ratio()
t2 = time()
print("a.i.r",b, b[0] / b[1])
t3 = time()
print("f.t.r",float_to_ratio(a))
t4 = time()
print("f.r",f_r(a))
t5 = time()
print("f.r2",f_r2(flt=c[0], prc=c[1], rep=c[2]))
t6 = time()
print("f.r3",f_r3(c[0], c[2]))
t7 = time()
print("f.t.r2",f_to_r(a))
t8 = time()
print(t2 - t1, t4 - t3, t5 - t4, t6 - t5, t7 - t6, t8 - t7)
