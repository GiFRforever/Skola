import pylab as pl

# Data pro první graf
x1 = pl.arange(0, 5, 0.1)
y1 = pl.exp(-x1) * pl.cos(2 * pl.pi * x1)

# Data pro druhý graf
x2 = pl.arange(0, 5, 0.02)
y2 = pl.cos(2 * pl.pi * x2)

# Vykreslení grafů
pl.subplot(2, 1, 1)
pl.plot(x1, y1, 'k-', linewidth=1)
pl.scatter(x1, y1, c='b', marker='o', s=16)
pl.grid(True)

pl.subplot(2, 1, 2)
pl.plot(x2, y2, 'r--', linewidth=1)
pl.grid(True)

pl.show()
