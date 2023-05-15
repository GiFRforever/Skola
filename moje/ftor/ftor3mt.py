import multiprocessing as mp


def ftor(flt: float, proc: int) -> list[int]:
    jádra: int = mp.cpu_count()
    délka: int = 50000000
    try:
        primes == []  # type: ignore
        print("Primes already loaded.")
    except:
        primes: list[int] = []
        with open("moje/p/primes.txt", "r") as f:
            print(f"Inicializace listu {proc}")
            f.seek((délka // jádra) * proc)
            if proc == jádra - 1:
                kolik = 50000000 - (délka // jádra) * (jádra - 1)
            else:
                kolik = délka // jádra
            for i in range(kolik):
                primes.append(int(f.readline()))
            print(f"List {proc} inicializován")

    if flt == int(flt):
        return [1]
    flt_split: list[str] = str(flt).split(".")
    num: int = int("".join(flt_split))
    den: int = 10 ** len(flt_split[1])
    out: list[int] = []
    n: int = 0
    m: int = 0
    while m == 0:
        while n == 0:
            for i in primes:  # type: ignore
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
    return out


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
    pool = mp.Pool(processes=jádra)

    def f(flt) -> list[int]:
        return [
            item
            for sublist in pool.starmap(ftor, zip(flt, range(jádra)))
            for item in sublist
        ]

    """print("Inicializace...")
    f([0]*jádra)
    print("Inicializace dokončena.")"""

    while True:
        flt: list[float] = [vstup_float("Zadejte číslo: ")] * jádra
        """deviders: list[int] = f(flt)
        deviders.sort()
        print(deviders)"""
        flt_split: list[str] = str(flt[0]).split(".")
        num: int = int("".join(flt_split))
        den: int = 10 ** len(flt_split[1])
        for i in f(flt):
            num //= i
            den //= i
        print(f"{flt[0]} = {num}/{den}")
