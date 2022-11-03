import multiprocessing as mp
from time import sleep
import re

def ftor(proc: int, jádra: int, conn) -> list[int]:
    délka: int = 50000000
    """try:
        if primes == []:
            pass
        print("Primes already loaded.")
    except:"""
    primes: list[int] = []
    with open("moje/p/primes.txt", "r") as f:
        print(f"Inicializace listu {proc}")
        f.seek((délka//jádra)*proc)
        if proc == jádra-1:
            kolik = 50000000 - (délka//jádra)*(jádra-1)
        else:
            kolik = délka//jádra
        for i in range(kolik):
            primes.append(int(f.readline()))
        print(f"List {proc} inicializován")
    
    while True:

        cislo: int = conn.recv()
        """if flt == int(flt):
            return [1]"""
        """flt_split: list[str] = str(flt).split(".")
        num: int = int("".join(flt_split))
        den: int = 10 ** len(flt_split[1])"""
        out: list[int] = []
        n: int = 0
        m: int = 0
        while m == 0:
            while n == 0:
                for i in primes:
                    if cislo % i == 0:
                        out.append(i)
                        cislo //= i
                        n = 1
                        break
                if n == 1:
                    n = 0
                    continue
                m = 1
                break
        conn.send(out)

def vstup_list(txt: str) -> list[int]:
    bu: str = " "
    while True:
        try:
            bu: str = input(txt)
            return list(map(int, re.split(",|.| ", bu)))
        except ValueError:
            if bu != "":
                if bu[0] == "q":
                    exit()
                return list(map(int, re.split(",|.| ", bu)))
            print("Zadejte čísla!")

if __name__ == "__main__":
    jádra: int = mp.cpu_count()
    print(f"Počet jáder: {jádra}")
    for i in range(jádra): # init pri kazdem startu
        globals()[f"pipe_p_{i}"], globals()[f"pipe_c_{i}"] = mp.Pipe() 
        globals()[f"prcs{i}"] = mp.Process(target=ftor, args=(i, jádra, globals()[f"pipe_c_{i}"]))
        globals()[f"prcs{i}"].start()
        globals()[f"pipe_c_{i}"].send(0)
        print(globals()[f"pipe_p_{i}"].recv()) # tady udělat čekání
    
    while True:
        vst_list: list[int] = vstup_list("Zadejte čísla: ")
        for cis, key in zip(vst_list, range(len(vst_list))):
            for i in range(jádra):
                globals()[f"pipe_c_{i}"].send(cis)
            globals()[f"deviders_{key}"] = []
            for i in range(jádra):
                globals()[f"deviders_{key}"].append([item for sublist in globals()[f"pipe_p_{i}"].recv() for item in sublist])
        # vvv tady poděl itemi z flt devideri a pak zobraz výslednou změnu
        deviders = []
        for i in range(1,len(vst_list)):
            deviders.append([set(globals()[f"deviders_{i}"])&set(globals()[f"deviders_{i-1}"])])
        print(deviders)
        """flt_split: list[str] = str(flt).split(".")
        num: int = int("".join(flt_split))
        den: int = 10 ** len(flt_split[1])
        for i in deviders:
            num //= i
            den //= i
        print(f"{flt} = {num}/{den}")"""