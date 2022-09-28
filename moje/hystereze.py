def vstup(txt):
    cislo = int(input(txt))
    return cislo

"""
with open("primes.txt", "r") as f:
    primes = [int(p) for p in f]


def comd(num, den):
    for i in primes:
        if num % i == 0:
            if den % i == 0:
                return i
    return 0


def f_to_r2(flt):
    if int(flt) == flt:
        return int(flt), 1
    flt_str = str(flt)
    flt_split = flt_str.split(".")
    num = int("".join(flt_split))
    den = 10 ** len(flt_split[1])
    devs = []
    while True:
        cdt = comd(num, den)
        if cdt != 0:
            num = num / cdt
            den = den / cdt
            devs.append(cdt)
        else:
            comdev = 1
            for i in devs:
                comdev = comdev * i
            return int(num), int(den)
"""
def f_r2(flt:float, prc=0, rep=100000):
    # print(flt,prc,rep)
    num: int = 1
    den: int = 1
    rat: float = num / den

    if prc != 0:
        flt = round(flt, prc)
    elif prc == -1:
        if flt > 0:
            for i in range(0, rep):
                while rat > flt:
                    den += 1
                    rat = num / den
                while rat < flt:
                    num += 1
                    rat = num / den
                # print(rat)
        else:
            for i in range(0, rep):
                while rat < flt:
                    den += 1
                    rat = num / den
                while rat > flt:
                    num -= 1
                    rat = num / den
                # print(rat)
        return str(num) + "/" + str(den)
	
    if flt > 0:
        while rat != flt:
            while rat > flt:
                den += 1
                rat = num / den
            while rat < flt:
                num += 1
                rat = num / den
            # print(rat)
    else:
        while rat != flt:
            while rat < flt:
                den += 1
                rat = num / den
            while rat > flt:
                num -= 1
                rat = num / den
            # print(rat)
    return str(num)+"/"+str(den)


def calc_parabola_vertex(x1, y1, x2, y2, x3, y3) -> tuple[float, float, float]:
    denom: float = (x1 - x2) * (x1 - x3) * (x2 - x3)
    A: float = (x3 * (y2 - y1) + x2 * (y1 - y3) + x1 * (y3 - y2)) / denom
    B: float = (x3 * x3 * (y1 - y2) + x2 * x2 * (y3 - y1) + x1 * x1 * (y2 - y3)) / denom
    C: float = (x2 * x3 * (x2 - x3) * y1 + x3 * x1 * (x3 - x1) * y2 + x1 * x2 * (x1 - x2) * y3) / denom
    return A, B, C


x1: int = -20
y1: float = vstup("Vrchol: ")
y3 = x2 = y2 = vstup("Křivka: ")
x3 = -40 - x2
a, b, c = calc_parabola_vertex(x1, y1, x2, y2, x3, y3)
print(x1, y1, x2, y2, x3, y3)
print("a={0}, b={1}, c={2}".format(a, b, c))
ar: str = f_r2(a)
br: str = f_r2(b)
cr: str = f_r2(c)
print("a={0} b={1} c={2}".format(ar, br, cr))
print("https://www.wolframalpha.com/input?i=plot+{}x^2%2B{}x%2B{}%3Dy".format(ar, br, cr))
if input("Plot? [Yes/No]: ") == "Yes":
	import matplotlib.pyplot as plt
	import numpy as np
	x = np.linspace(x1, x2, 1000)
	y = a * x ** 2 + b * x + c
	plt.title("Hystereze topení") 
	plt.xlabel("venkovní teplota [°C]")
	plt.ylabel("teplota okruhu [°C]")
	plt.plot(x, y)
	plt.show(block=True)