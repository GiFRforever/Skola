import pylab as pl

# 1
pl.subplot(2, 2, 1)
pl.grid(True)
pl.xlim(0, 10)
pl.ylim(0, 10)
pl.plot([1, 3, 5, 7, 9], [1, 6, 2, 6, 1], "r", linewidth=4)

# 2
pl.subplot(2, 2, 2)
pl.grid(True)
pl.xlim(-5, 10)

x = pl.linspace(-5, 10, 300)
y1 = 2 * x - 1
y2 = -2 * x + 1

pl.plot(x, y1, "g", label="y1=2x-1")
pl.plot(x, y2, "g", label="y2=-2x+1")

pl.fill_between(x, y1, y2, where=(x > 0), color="gray", alpha=0.5)
pl.legend()

# 3
pl.subplot(2, 2, 3)
pl.grid(True)
pl.xlim(-1, 6)
pl.ylim(-1, 6)
pl.plot([1, 1, 4, 4, 1], [1, 4, 4, 1, 1], "purple", linewidth=3)

# 4
pl.subplot(2, 2, 4)
pl.grid(True)
pl.xlim(-3, 3)
#pl.ylim(-6, 2)
x = pl.linspace(-3, 3, 100)
y = x**2 - 2 * x - 3
pl.plot(x, y, "black", label="y=x^2-2x-3")
pl.fill_between(x, y, color="lightgreen", alpha=0.5)
pl.legend()

pl.subplots_adjust(hspace=0.3, wspace=0.3)
pl.show()
