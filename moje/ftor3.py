from random import random
from time import time

primes_list: list[int] = []
primes_file: str = "moje/p/primes.txt"

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

def main(r = 16) -> float:
    floutik: float = vstup_float("flt:")
    """
    floutik: float = round(random(), r)
    c: list[float | int] = []
    p: int = vstup_int_modified("prc [def: 0 -> rep, -1 -> precise]: ")
    r: int = vstup_int_modified("rep [def: 1000000]: ")
    s: int = vstup_int_modified("search metod [def: 0 -> file, 1 -> list]: ")
    if p == 0:
        c.append(0)
    else:
        c.append(p)
    if r == 0:
        c.append(10000)
    else:
        c.append(r)
    c.append(round(random(), r))
    c.append(0)
    c.append(10000000)
    c.append(2)
    """
    #print(c)
    # vvv testovací funkce
    back: tuple[int, int, float] = (ftor_primes(floutik))
    print(back)
    return back[2] - floutik

def load_primes()  -> None:
    """Load primes from file."""
    global primes_list
    try:
        if primes_list[0] == 2:
            return
    except IndexError:
        pass
    print("Loading primes...")
    with open(primes_file, "r") as f:
        data: str = f.read()
        primes_list = [int(x) for x in data.split("\n")]
        print("Primes loaded.")

def load_primes_lists(lenght: int = 9) -> None:
    """Load primes lists."""
    if lenght > 9:
        lenght = 9
    for x in range(1, lenght + 1):
        try:
            if globals()["primes_list_" + str(x)][0]:
                continue
        except KeyError:
            pass
        with open(f"moje/p/primes{x}.txt", "r") as f:
            globals()["primes_list_" + str(x)] = [int(i) for i in f.read().split("\n") if len(i) == x]
            print(f"primes_list_{x} loaded")
            #breakpoint()

def load_primes_lists2() -> None:
    """Load primes lists."""
    for x in range(8, 10):
        try:
            if globals()["primes_list_" + str(x)][0]:
                continue
        except:
            pass
    with open(primes_file, "r") as f:
        globals()["primes_list_s"] = [int(i) for i in f.read().split("\n") if len(i) < 9]
        print("primes_list_s loaded")
        globals()["primes_list_l"] = [int(i) for i in f.read().split("\n") if len(i) == 9]
        print("primes_list_l loaded")
        #breakpoint()
def load_primes_lists3() -> None:
    """Load primes lists."""
    with open(primes_file, "r") as f:
        globals()["primes_list_s"] = [int(i) for i in f.read().split("\n") if len(i) < 9]
        globals()["primes_list_l"] = [int(i) for i in f.read().split("\n") if len(i) == 9]
        print("primes_lists3 loaded")
        #breakpoint()
"""
def ftor_repetitive(flt: float, rep: int) -> tuple[int, int, float]:
    #Ftor for repetitive approximation.
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
"""
def ftor_primes(flt: float,) -> tuple[int, int, float]:
    """Ftor for primes approximation."""
    global primes_list
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
    if len(str(min(num, den))) > 8:
        search_method = 2
    else:
        search_method = 0
    #print(num, den)
    if search_method == 0:
        #global primes_list_s
        n: int = 0
        m: int = 0
        load_primes()
        while n == 0:
            for i in primes_list:
                #print(i)
                if i > num:
                    m = 1
                    n += 1
                    break
                if num % i == 0 and den % i == 0:
                    num //= i
                    den //= i
                    #print(i)
                    #if n == 1:
                    #    print("What the fuck?", flt)
                    m = 1
                    break
            if m == 1: m = 0 ; continue
            #print("Just a sec...")
            n += 1
    elif search_method == 1:
        #breakpoint()
        for x in range(1, len(str(min(num, den))) + 1):
            if x > len(str(min(num, den))) or x > 9:
                break
            load_primes_lists(x)
            n: int = 0
            m: int = 0
            while n == 0:
                for i in globals()["primes_list_" + str(x)]:
                    if num % i == 0 and den % i == 0:
                        num //= i
                        den //= i
                        m = 1
                    if m == 1: break
                if m == 1: m = 0 ; continue
                n += 1
    elif search_method == 2:
        #breakpoint()
        for x in ["s", "l"]:
            #load_primes_lists2()
            n: int = 0
            m: int = 0
            while n == 0:
                for i in globals()["primes_list_" + x]:
                    if num % i == 0 and den % i == 0:
                        num //= i
                        den //= i
                        m = 1
                    if m == 1: break
                if m == 1: m = 0 ; continue
                n += 1
    """
    elif search_method == 3:
        n: int = 0
        m: int = 0
        global primes_list_s
        global primes_list_l
        while n == 0:
            for i in primes_list_s:
                if num % i == 0 and den % i == 0:
                    num //= i
                    den //= i
                    m = 1
                if m == 1: break
            if m == 1: m = 0 ; continue
            n += 1
        if len(str(min(num, den))) >= 9:
            n: int = 0
            m: int = 0
            while n == 0:
                for i in primes_list_l:
                    if num % i == 0 and den % i == 0:
                        num //= i
                        den //= i
                        m = 1
                    if m == 1: break
                if m == 1: m = 0 ; continue
                n += 1
    else:
        n: int = 0
        m: int = 0
        while n == 0:
            with open(primes_file, "r") as primes:
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
                        #if n == 1:
                        #    print("What the fuck?", flt)
                        m = 1
                        break
                if m == 1: m = 0 ; continue
                #print("Just a sec...")
                n += 1
    """
    return sign * num, den, sign * num / den

#load_primes_lists(8)
load_primes_lists2()
load_primes()

while True:
    print(main())
"""

test_samples:int = 10
for i in range(1, 17, 1):
    odchylka: list[float] = []
    t1: float = time()
    for x in range(0, test_samples):
        odchylka.append(main(i))
    t2: float = time()
    průměrná_odchylka: float = sum(odchylka) / len(odchylka)
    čas: float = (t2 - t1) / test_samples
    print(f"Pro {i} desetinných míst je průměrná odchylka {průměrná_odchylka} a časem {čas}.")
    #with open("moje/temp2.txt", "w") as f:
    #    f.write(f"{i}, {průměrná_odchylka}, {čas}")
"""