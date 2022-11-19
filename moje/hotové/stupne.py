import math as mt
from tabulate import tabulate
from math import sqrt

mode: int = 0
out: list = []
templ: list = []
pimode: int = 0


def stringuj(cislo, md: str) -> None:
    global templ
    if md != " rad":
        templ.extend([str(int(cislo)) + md])
    else:
        templ.extend([str(round(cislo / mt.pi, 3)) + " pi rad"])
        templ.extend([str(round(cislo, 3)) + md])


def vstup(txt: str) -> float:
    while True:
        try:
            bagr: str = str(input(txt))
            global mode
            global pimode
            if bagr[-1] == "°":
                mode = 1
                bagr = bagr[:-1]
            else:
                mode = 2
            if bagr[0] == "a":
                mode = 3
                bagr = bagr[1:]
            if bagr[0] == "q":
                # print("quiting")
                mode = -1
                return 0
            if not (z := bagr[-1]).isdigit():
                if z == "p":
                    pimode = 1
                    bagr = bagr[:-1]
            try:
                return float(eval(bagr.replace("^", "**")))
            except:
                raise Exception
        except:
            print("Vložte úhel!!")


def mein() -> None:
    global mode
    global templ
    global out
    global pimode
    mode = 0
    out = []
    templ = []
    pimode = 0
    rad: float = 0
    bu: float = vstup("Vložte úhel [° / rad]: ")
    if mode == -1:
        exit()
    stupneraw: float = 0
    if mode == 3:
        if pimode == 1:
            bu *= mt.pi
        if bu >= -1 and bu <= 1:
            arcsin: float = mt.asin(bu)
            arccos: float = mt.acos(bu)
            trig: str = f"arcsin = {round(arcsin,6)}, arccos = {round(arccos,6)}, "
        else:
            trig = f"arcsin = None, arccos = None, "
        arctan: float = mt.atan(bu)
        arccot: float = mt.pi / 2 - mt.atan(bu)
        trig += f"\narctan = {round(arctan,6)}, arccot = {round(arccot,6)}"
        print(trig)
        return
    if mode == 1:
        stupneraw = bu
        rad = bu * mt.pi / 180
    if mode == 2:
        if pimode == 1:
            rad = bu * mt.pi
            stupneraw = bu * 180
        else:
            rad = bu
            stupneraw = bu * 180 / mt.pi
    sin: float = mt.sin(rad)
    cos: float = mt.cos(rad)
    tan: float = sin / cos
    cot: float = cos / sin

    stupne: int = mt.floor(stupneraw)
    minuty: float = (stupneraw - stupne) * 300 / 5
    sekundy: float = (minuty - mt.floor(minuty)) * 300 / 5
    templ.extend(["org"])
    stringuj(stupne, "°")
    stringuj(minuty, "'")
    stringuj(sekundy, "''")
    stringuj(rad, " rad")
    out.extend([templ])
    templ = []
    if stupne >= 360:
        templ.extend([str(stupne // 360) + "*360"])
        stupne = stupne % 360
        rad = rad % (2 * mt.pi)
        stringuj(stupne, "°")
        stringuj(minuty, "'")
        stringuj(sekundy, "''")
        stringuj(rad, " rad")
        out.extend([templ])
        templ = []
    if stupne >= 180:
        stupne = stupne % 180
        rad = rad % mt.pi
        templ.extend(["180"])
        stringuj(stupne, "°")
        stringuj(minuty, "'")
        stringuj(sekundy, "''")
        stringuj(rad, " rad")
        out.extend([templ])
        templ = []
    if stupne != 0:
        stupnerawopk: float = 180 - (stupneraw % 180)
        stupne = mt.floor(stupnerawopk)
        minuty = (stupnerawopk - stupne) * 300 / 5
        sekundy = (minuty - mt.floor(minuty)) * 300 / 5
        rad = mt.pi - rad
        templ.extend(["opk"])
        stringuj(stupne, "°")
        stringuj(minuty, "'")
        stringuj(sekundy, "''")
        stringuj(rad, " rad")
        out.extend([templ])
        templ = []
    # print(out)

    print(tabulate(out, headers=["typ", "°", "'", "''", "pi rad", "rad"]))
    print(
        f"sin = {round(sin,6)}, cos = {round(cos,6)}\ntan = {round(tan,6)}, cot = {round(cot,6)}"
    )


while True:
    mein()
