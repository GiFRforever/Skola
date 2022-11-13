from time import time
from random import random
import shutil

#If you want to run it, you need to create a folder called "primes" and put the two files "primess.txt" and "primesl.txt" in it. You can get them here:
primes_dir: str = "moje/p/"
primes_list_s = primes_list_l = []

def vstup_float(txt) -> float:
    bu = " "
    global search_mode
    search_mode = 1
    while True:
        try:
            bu: str = input(txt)
            return float(bu)
        except ValueError:
            if bu != "":
                if bu[0] == "s":
                    search_mode = 3
                    bu = bu[1:]
                if bu[0] == "l":
                    search_mode = 2
                    bu = bu[1:]
                if bu[0] == "t":
                    bu = bu[1:]
                    try:
                        test(int(bu))
                    except:
                        test()
                if bu[0] == "q":
                    exit()
                return float(bu)
            print("Zadejte číslo!")
def init(what = 0) -> None:
    global primes_list_s, primes_list_l
    if what == 0 or what == 1:
        if primes_list_s == []:
            print("Loading small primes...")
            with open(primes_dir+"primess.txt", "r") as f:
                primes_list_s = [int(i) for i in f.read().split("\n")]
            print("Primes loaded.")
    if what == 0 or what == 2:
        if primes_list_l == []:
            print("Loading large primes...")
            with open(primes_dir+"primesl.txt", "r") as f:
                primes_list_l = [int(i) for i in f.read().split("\n")]
            print("Primes loaded.")
def ftor_primes(flt: float) -> tuple[int, int, float]:
    global primes_list_s, primes_list_l, search_mode
    if search_mode == 3:
        print(search_prime(flt))
        return (0, 0, 0)
    if flt == int(flt):
        return int(flt), 1, int(flt)
    if flt < 0:
        flt = -flt
        sign: int = -1
    else:
        sign = 1
    flt_split: list[str] = str(flt).split(".")
    num: int = int("".join(flt_split))
    den: int = 10 ** len(flt_split[1])
    #for x in ["s", "l"]:
    if primes_list_s == []:
        init(1)
    n: int = 0
    m: int = 0
    while n == 0:
        for i in primes_list_s:
            if num % i == 0 and den % i == 0:
                num //= i
                den //= i
                m = 1
            if m == 1: break
        if m == 1: m = 0 ; continue
        n += 1
    if len(str(min(num, den))) < 9 or search_mode == 1:
        return sign * num, den, sign * num / den
    if primes_list_l == []:
        init(2)
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
    acc: int = 2
    pnum: list[int] = search_prime(num, acc)
    pden: list[int] = search_prime(den, acc)
    #print(pnum, pden)
    devidor: int = 1
    for i in set(pnum) & set(pden):
        #print(i)
        devidor *= i
    num //= devidor
    den //= devidor
    if den == 0 or num == 0:
        #print("Error: dev0")
        return 0, 0, 0
    return sign * num, den, sign * num / den
def test(test_samples:int = 100) -> None:
    init()
    for i in range(1, 17, 1):
        breakpoint()
        odchylka: list[float] = []
        printProgressBar(0, test_samples, prefix = f"Progress ({i}/16):", suffix = 'Complete', autosize = True)
        t1: float = time()
        global search_mode
        search_mode = 2
        for x in range(0, test_samples):
            floutik: float = round(random(), i)
            odchylka.append(ftor_primes(floutik)[2]-floutik)
            printProgressBar(x + 1, test_samples, prefix = f"Progress ({i}/16):", suffix = 'Complete', autosize = True)
        t2: float = time()
        průměrná_odchylka: float = sum(odchylka) / len(odchylka)
        čas: float = (t2 - t1) / test_samples
        print(f"Pro {i} desetinných míst je průměrná odchylka {průměrná_odchylka} a časem {čas}.")
def main() -> tuple[int, int, float]:
    floutik: float = vstup_float("float:")
    back: tuple[int, int, float] = (ftor_primes(floutik))
    print(f"{back[0]}/{back[1]} = {back[2]}")
    return back
def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', autosize = False):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        autosize    - Optional  : automatically resize the length of the progress bar to the terminal window (Bool)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    styling = '%s |%s| %s%% %s' % (prefix, fill, percent, suffix)
    if autosize:
        cols, _ = shutil.get_terminal_size(fallback = (length, 1))
        length = cols - len(styling) -3
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s' % styling.replace(fill, bar), end = '\r')
    # Print New Line on Complete
    if iteration == total: 
        print("\r")
def search_prime(cislo, acc: int = 1) -> list[int]:
    init(1)
    if int(cislo) in primes_list_s:
        return cislo
    init(2)
    if int(cislo) in primes_list_l:
        return cislo
    out: list[int] = []
    for i in reversed(primes_list_l):
        if cislo % i < acc:
            out.append(i)
    for i in reversed(primes_list_s):
        if cislo % i < acc:
            out.append(i)
    return out
if __name__ == "__main__":
    while True:
        main()
