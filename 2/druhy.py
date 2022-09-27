# from math import *
from tabulate import tabulate

out = []
for i in range(100, -1, -10):
    a = int(10 ** (i / 10))
    out.extend([[i, a]])
print(tabulate(out, headers=["dB", "P"]))
