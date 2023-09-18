from math import *

mode = 0


def vstup(txt: str) -> float:
    bagr = None
    while bagr is None:
        try:
            bagr = str(input(txt))
            global mode
            if bagr[-1] == "°":
                mode = 1
            elif bagr[-1] == "d":
                mode = 2
            else:
                bagr = None
                raise Exception
            for z in reversed(bagr):
                if not z.isdigit():
                    bagr = bagr[:-1]
                else:
                    try:
                        return float(bagr)
                    except:
                        bagr = None
                        raise Exception
        except:
            print("Vložte úhel!!")


bu = vstup("Vložte úhel [° / rad]: ")
if mode == 1:
    print("sin ", bu, "° = ", sin(radians(bu)))
    print("cos ", bu, "° = ", cos(radians(bu)))
if mode == 2:
    print("sin ", bu, " rad = ", sin(bu))
    print("cos ", bu, " rad = ", cos(bu))
