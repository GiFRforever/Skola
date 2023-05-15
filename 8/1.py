import math
import time


def main():
    try:
        a, b, c = eval(input("Please enter the coefficients (a, b, c): "))
    except:
        print("\033[91m Neplatný vstup\033[0m", end="\r")
        time.sleep(1)
        return
    if a == 0:
        if b == 0:
            if c == 0:
                print("\033[93m Rovnice je lineární, má nekonečně mnoho řešení\033[0m")
                return
            else:
                print("\033[91m Rovnice nemá řešení\033[0m")
                return
        else:
            if c == 0:
                print(f"\033[93m Rovnice je lineární, x = 0\033[0m")
                return
            else:
                print(f"\033[93m Rovnice je lineární, x = {-c/b}\033[0m")
                return
    d = b * b - 4 * a * c
    if d < 0:
        print("\033[91mRovnice nemá řešení v oboru R\033[0m")
        return
    discRoot = math.sqrt(d)
    root1 = (-b + discRoot) / (2 * a)
    if d == 0:
        print("\033[92mRovnice má jedno řešení: ", root1, "\033[0m")
        return
    root2 = (-b - discRoot) / (2 * a)
    print("\033[92mRovnice má dvě řešení:", root1, root2, "\033[0m")


if __name__ == "__main__":
    print("Řešení kvadratické rovnice v R")
    while True:
        main()
