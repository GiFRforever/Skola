import multiprocessing as mp
from random import randint, random
from time import sleep

def ftor(proc: int, jádra: int, conn) -> None:
    délka: int = 50000000
    primes: list[int] = []
    with open("moje/p/primes.txt", "r") as f:
        print(f"Inicializace listu {proc}", end="\r")
        f.seek((délka//jádra)*proc)
        if proc == jádra-1:
            kolik: int = 50000000 - (délka//jádra)*(jádra-1)
        else:
            kolik = délka//jádra
        for i in range(kolik):
            primes.append(int(f.readline()))
        #print(f"List {proc} inicializován", end="\r")
        conn.send("OK")
    
    while flt := conn.recv() is not None:
        flt: float = conn.recv()
        #print(f"Process {proc} received {flt}")
        if flt == int(flt):
            conn.send([1,1])
        flt_split: list[str] = str(flt).split(".")
        num: int = int("".join(flt_split))
        den: int = 10 ** len(flt_split[1])
        out: list[int] = []
        n: int = 0
        m: int = 0
        while m == 0:
            while n == 0:
                for i in primes:
                    if num % i == 0:
                        if den % i == 0:
                            #print(f"Process {proc} found {i}")
                            out.append(i)
                            num //= i
                            den //= i
                            n = 1
                            break
                if n == 1:
                    n = 0
                    continue
                m = 1
                break
        conn.send(out)

def vstup_float(txt: str) -> float:
    bu: str = " "
    while True:
        try:
            bu = input(txt)
            da: float = float(bu.replace(",",".").strip())
            #print(da)
            if da == int(da):
                print("\033[91mZadejte desetinné číslo!\033[0m", end="\r")
                sleep(1)
                print("                            ", end="\r")
                continue
            else:
                return da
        except:
            if bu != "":
                if bu[0] == "q":
                    for i in range(jádra):
                        globals()[f"prcs{i}"].terminate()
                    exit()
                print("Zadejte číslo nebo q pro ukončení.")
                continue
            print("\033[91mZadejte číslo!\033[0m", end="\r")
            sleep(0.5)

if __name__ == "__main__":
    jádra: int = mp.cpu_count()
    print(f"Počet jáder: {jádra}", end="\r")
    for i in range(jádra):
        globals()[f"pipe_p_{i}"], globals()[f"pipe_c_{i}"] = mp.Pipe() 
        globals()[f"prcs{i}"] = mp.Process(target=ftor, args=(i, jádra, globals()[f"pipe_c_{i}"]))
        globals()[f"prcs{i}"].start()
    
    sleep(1)
    print(f"Počet jáder: {jádra}      ", end="\r")
    sleep(1)
    print("Loading...           ", end="\r")
    for i in range(jádra):
        print(globals()[f"pipe_p_{i}"].recv(), end="\r")
    print("Loaded.              ", end="\r")

    while True:
        flt: float = vstup_float("Zadejte číslo: ")
        for i in range(jádra):
            globals()[f"pipe_p_{i}"].send(1) # starts while loop
            globals()[f"pipe_p_{i}"].send(float(flt))
        deviders: list[int] = []
        for i in range(jádra):
            ingested: list = globals()[f"pipe_p_{i}"].recv()
            #print(ingested)
            for itm in ingested:
                deviders.append(int(itm))
        #print(deviders)
        flt_split: list[str] = str(flt).split(".")
        num: int = int("".join(flt_split))
        den: int = 10 ** len(flt_split[1])
        for i in deviders:
            num //= i
            den //= i
        print(f"{num/den} = {num}/{den}")
        #print(f"Vydáno: {num/den}, {flt-num/den}")

#tenhle je ten konečnej