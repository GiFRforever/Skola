import pylab as pl

x = pl.linspace(0, 10, 20)
y = x**3 - 2 * x**2 + x - 1
pl.plot(x, y)
pl.plot(x, y, "o")
pl.show()
