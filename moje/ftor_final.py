primes_dir: str = "moje/p/"
from time import time
from random import random

def vstup_float(txt) -> float:
    while True:
        try:
            bu: str = input(txt)
            return float(bu)
        except ValueError:
            if bu == "t": # type: ignore
                test()
            print("Zadejte číslo!")
def init() -> None:
    print("Loading primes...")
    with open(primes_dir+"primesl.txt", "r") as f:
        globals()["primes_list_l"] = [int(i) for i in f.read().split("\n")]
    print("Just a sec...")
    with open(primes_dir+"primess.txt", "r") as f:
        globals()["primes_list_s"] = [int(i) for i in f.read().split("\n")]
    print("Primes loaded.")
def ftor_primes(flt: float) -> tuple[int, int, float]:
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
    for x in ["s", "l"]:
        if len(str(min(num, den))) > 8 and x == "l" or x == "s":
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
    return sign * num, den, sign * num / den
def test() -> None:
    test_samples:int = 100
    for i in range(1, 17, 1):
        odchylka: list[float] = []
        t1: float = time()
        for x in range(0, test_samples):
            floutik: float = round(random(), i)
            odchylka.append(ftor_primes(floutik)[2]-floutik)
        t2: float = time()
        průměrná_odchylka: float = sum(odchylka) / len(odchylka)
        čas: float = (t2 - t1) / test_samples
        print(f"Pro {i} desetinných míst je průměrná odchylka {průměrná_odchylka} a časem {čas}.")
def main() -> tuple[int, int, float]:
    floutik: float = vstup_float("float:")
    back: tuple[int, int, float] = (ftor_primes(floutik))
    print(f"{back[0]}/{back[1]} = {back[2]}")
    return back

init()
while True:
    main()