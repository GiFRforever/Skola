import multiprocessing as mp
from time import sleep

def ftor(proc: int, jádra: int, conn) -> None:
    """try:
        primes == []
        print("Primes already loaded.")
    except:"""
    délka: int = 50000000
    primes: list[int] = []
    with open("moje/p/primes.txt", "r") as f:
        print(f"Inicializace listu {proc}")
        f.seek((délka//jádra)*proc)
        if proc == jádra-1:
            kolik: int = 50000000 - (délka//jádra)*(jádra-1)
        else:
            kolik = délka//jádra
        for i in range(kolik):
            primes.append(int(f.readline()))
        print(f"List {proc} inicializován")
        conn.send("OK")
    
    while fltv := conn.recv() is not None:
        flt: float = float(fltv)
        if type(flt) == float:
            print(flt)
        elif type(flt) == int:
            print(flt," je int")
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
            bu: str = input(txt)
            bu.replace(",",".")
            return float(bu)
        except:
            if bu != "":
                if bu[0] == "q":
                    for i in range(jádra):
                        globals()[f"prcs{i}"].terminate()
                    exit()
                return float(bu)
            print("Zadejte číslo!")

if __name__ == "__main__":
    jádra: int = mp.cpu_count()
    print(f"Počet jáder: {jádra}")
    for i in range(jádra):
        globals()[f"pipe_p_{i}"], globals()[f"pipe_c_{i}"] = mp.Pipe() 
        globals()[f"prcs{i}"] = mp.Process(target=ftor, args=(i, jádra, globals()[f"pipe_c_{i}"]))
        globals()[f"prcs{i}"].start()
        #globals()[f"pipe_c_{i}"].send(0)
        #print(globals()[f"pipe_p_{i}"].recv()) # tady udělat čekání
    
    for i in range(jádra):
        print(globals()[f"pipe_p_{i}"].recv())
    
    while True:
        flt: float = vstup_float("Zadejte číslo: ")
        for i in range(jádra):
            globals()[f"pipe_p_{i}"].send(flt)
        deviders: list[int] = []
        for i in range(jádra):
            ingested: list = globals()[f"pipe_p_{i}"].recv()
            print(ingested)
            for itm in ingested:
                deviders.append(int(itm))
            #deviders.append([item for sublist in globals()[f"pipe_p_{i}"].recv() for item in sublist])
        print(deviders)
        flt_split: list[str] = str(flt).split(".")
        num: int = int("".join(flt_split))
        den: int = 10 ** len(flt_split[1])
        for i in deviders:
            num //= i
            den //= i
        print(f"{flt} = {num}/{den}")