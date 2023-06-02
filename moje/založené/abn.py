from math import sqrt
from time import time


def jejich(n) -> None:
    # n: int = int(input("n = "))
    out: list[str] = []
    t1: float = time()
    for a in range(0, n + 1):
        b = n - 2 * sqrt(n * a) + a
        if b.is_integer():
            out.append(f"\na = {a} b = {b}")
    t2: float = time()
    print(*out)
    print(f"Time: {t2 - t1}")


def moje(n) -> None:
    # n: int = int(input("n = "))
    t1: float = time()
    out_a: list[int] = []
    for a in range(0, n + 1):
        if is_square(n * a):  # or is_square(4*n*a) <- not needed
            out_a.append(a)
    out: list[str] = [f"\na = {a} b = {b}" for a, b in zip(out_a, out_a[::-1])]
    t2: float = time()
    print(*out)
    print(f"Time: {t2 - t1}")


def is_square(apositiveint) -> bool:
    x: int = apositiveint // 2
    seen: set[int] = set([x])
    while x * x != apositiveint:
        x = (x + (apositiveint // x)) // 2
        if x in seen:
            return False
        seen.add(x)
    return True


if __name__ == "__main__":
    n = int(input("n = "))
    jejich(n)
    moje(n)
