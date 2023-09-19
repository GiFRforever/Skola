import pylab as pl

x_values = [0, 3, 5, 6]
y_values = [4, 3, 9, 5]

# x_values = [float(x) for x in input("Zadejte 4 hodnoty x oddělené mezerami: ").split()][:4]
# y_values = [float(y) for y in input("Zadejte 4 hodnoty y oddělené mezerami: ").split()][:4]

# x_values = []
# y_values = []
# for i in range(1, 5):
#    x = float(input("Vložte x({i}): "))
#    y = float(input("Vložte y({i}): "))
#    x_values.append(x)
#    y_values.append(y)

pl.subplot(2, 1, 1)
pl.plot(x_values, y_values, "g-", linewidth=2)
pl.scatter(x_values, y_values, marker="o", color="red", s=80)
pl.xlabel("X")
pl.ylabel("Y")
pl.grid(True)

x = pl.linspace(-2 * pl.pi, 2 * pl.pi, 500)
y1 = pl.sin(2 * x)
y2 = 2 * pl.cos(x)

pl.subplot(2, 1, 2)
pl.plot(x, y1, color="blue", label="y1 = sin(2x)")
pl.plot(x, y2, color="blue", linestyle="--", label="y2 = 2cos(x)")
pl.fill_between(x, y1, y2, interpolate=True, color="lightblue")
pl.xlabel("X")
pl.ylabel("Y")
pl.xlim(-2 * pl.pi, 2 * pl.pi)
pl.legend()
pl.grid(True)

pl.tight_layout()
pl.show()
