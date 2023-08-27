import pylab as pl
import random as rd

x = pl.array([rd.randint(0, 100) for _ in range(20)])
y = pl.array([rd.randint(0, 100) for _ in range(20)])

pl.axis([0, 100, 0, 100])

pl.plot(x, y, "s")

pl.show()
