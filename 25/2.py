import pylab as pl


def y1(x):
    return -(x - 2)**2 + 4

def y2(x):
    return -85 * x

x = pl.linspace(-100, 100, 100)

pl.plot(x, y1(x), label='y1 = -(x-2)^2 + 4')
pl.plot(x, y2(x), 'r--', linewidth=3, label='y2 = -85x')

pl.fill_between(x, y1(x), y2(x), where=(y1(x) > y2(x)), color='lightblue')

pl.annotate('A', (0,0), xytext=(0, 20), textcoords='offset points', arrowprops=dict(arrowstyle="->"))
pl.annotate('B', (89,-7565), xytext=(-30, -20), textcoords='offset points', arrowprops=dict(arrowstyle="->"))
pl.annotate("Střed", (43, -2346), xytext=(40,50),textcoords="offset points", arrowprops=dict(arrowstyle="->"))


pl.legend()
pl.show()
