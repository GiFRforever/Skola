from fileinput import close
from random import random
from time import time


def vstup_float(txt) -> float:
    while True:
        try:
            return float(input(txt))
        except ValueError:
            print("Zadejte číslo!")

def vstup_int_modified(txt) -> int:
    while True:
        try:
            vs: str = input(txt)
            if vs == "":
                return 0
            return int(vs)
        except ValueError:
            print("Zadejte číslo!")

def main(r) -> float:
    c: list[float | int] = []
    """
    c.append(vstup_float("flt:"))
    p: int = vstup_int_modified("prc [def: 0 -> rep, -1 -> precise]: ")
    r: int = vstup_int_modified("rep [def: 1000000]: ")
    if p == 0:
        c.append(0)
    else:
        c.append(p)
    if r == 0:
        c.append(10000)
    else:
        c.append(r)
    """
    c.append(round(random(), r))
    c.append(0)
    c.append(10000000)
    #print(c)
    # vvv testovací funkce
    back: tuple[int, int, float] = (ftor_primes(c[0]))
    #print(back)
    return back[2] - c[0]

def ftor_repetitive(flt: float, rep: int) -> tuple[int, int, float]:
    """Ftor for repetitive approximation."""
    if flt == int(flt):
        return int(flt), 1, 0
    if flt < 0:
        flt = -flt
        sign: int = -1
    else:
        sign = 1
    num: int = 1
    den: int = 1
    for i in range(rep):
        if num / den == flt:
            #print(i)
            return sign * num, den, sign * num / den
        elif num / den > flt:
            den += 1
        else:
            num += 1
    return sign * num, den, sign * num / den

def ftor_primes(flt: float) -> tuple[int, int, float]:
    """Ftor for primes approximation."""
    if flt == int(flt):
        return int(flt), 1, 0
    if flt < 0:
        flt = -flt
        sign: int = -1
    else:
        sign = 1
    flt_split: list[str] = str(flt).split(".")
    num: int = int("".join(flt_split))
    den: int = 10 ** len(flt_split[1])
    #print(num, den)
    n: int = 0
    m: int = 0
    while n == 0:
        with open("moje/p/primes.txt", "r") as primes:
            #primes: list[int] = [int(i) for i in f.readlines()]
            for i in primes:
                i = int(i)
                #print(i)
                if i > num:
                    m = 1
                    n += 1
                    break
                if num % i == 0 and den % i == 0:
                    num //= i
                    den //= i
                    #print(i)
                    if n == 1:
                        print("What the fuck?", flt)
                    m = 1
                    break
            if m == 1: m = 0 ; continue
            #print("Just a sec...")
            n += 1
    return sign * num, den, sign * num / den



#print(main(16))


for i in range(1, 17, 1):
    odchylka: list[float] = []
    t1: float = time()
    for x in range(0, 10):
        odchylka.append(main(i))
    t2: float = time()
    průměrná_odchylka: float = sum(odchylka) / len(odchylka)
    čas: float = (t2 - t1) / 10
    print(f"Pro {i} desetinných míst je průměrná odchylka {průměrná_odchylka} a časem {čas}.")
    #with open("moje/temp2.txt", "w") as f:
    #    f.write(f"{i}, {průměrná_odchylka}, {čas}")
