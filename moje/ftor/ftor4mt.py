import multiprocessing as mp
from time import sleep


def ftor(proc: int, jádra: int, conn) -> None:
    délka: int = 50000000
    """try:
        if locals()["primes"] != []:
            pass
        print("Primes already loaded.")
    except:"""
    primes: list[int] = []
    with open("moje/p/primes.txt", "r") as f:
        # print(f"Inicializace listu {proc}")
        f.seek((délka // jádra) * proc)
        if proc == jádra - 1:
            kolik: int = 50000000 - (délka // jádra) * (jádra - 1)
        else:
            kolik = délka // jádra
        for i in range(kolik):
            primes.append(int(f.readline()))
        # print(f"List {proc} inicializován")
        conn.send("OK")

    while len(primes) < délka // jádra:
        sleep(0.1)
    while (flt := conn.recv()) is not None:
        print(f"Process {proc} received {flt}")
        if flt == int(flt):
            conn.send([1])
            break
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
            return float(bu)
        except ValueError:
            if bu != "":
                if bu[0] == "q":
                    exit()
                return float(bu)
            print("Zadejte číslo!")


if __name__ == "__main__":
    jádra: int = mp.cpu_count()
    print(f"Počet jáder: {jádra}")
    """ init pri kazdem startu
    pool = mp.Pool(processes=jádra)
    def f(flt) -> list[int]:
        return [item for sublist in pool.starmap(ftor, zip(flt, range(jádra))) for item in sublist]
    """
    for i in range(jádra):
        globals()[f"pipe_p_{i}"], globals()[f"pipe_c_{i}"] = mp.Pipe()
        globals()[f"prcs{i}"] = mp.Process(
            target=ftor, args=(i, jádra, globals()[f"pipe_c_{i}"])
        )
        globals()[f"prcs{i}"].start()
        # globals()[f"pipe_c_{i}"].send(0)
        globals()[f"pipe_p_{i}"].recv()  # tady udělat čekání
    for i in range(jádra):
        if bu := globals()[f"pipe_p_{i}"].recv() == "OK":  # tady se čeká
            print(f"Process {i} OK")

    while True:
        flt: float = vstup_float("Zadejte číslo: ")
        """deviders: list[int] = f(flt)
        deviders.sort()
        print(deviders)"""
        for i in range(jádra):
            globals()[f"pipe_p_{i}"].send(flt)
        deviders: list = []
        for i in range(jádra):
            ingested: list = globals()[f"pipe_p_{i}"].recv()
            print(ingested)
            deviders.append(item for sublist in ingested for item in sublist)
        flt_split: list[str] = str(flt).split(".")
        num: int = int("".join(flt_split))
        den: int = 10 ** len(flt_split[1])
        for i in deviders:
            num //= i
            den //= i
        print(f"{flt} = {num}/{den}")
