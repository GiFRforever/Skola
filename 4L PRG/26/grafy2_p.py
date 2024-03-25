from tkinter import *
import pylab as pl
from tkinter import colorchooser
from tkinter import messagebox as msb

hlavni = Tk()
hlavni.title("Grafy")


def graf():
    global x_ove, y_ove, barva
    pl.plot(x_ove, y_ove, color=barva)
    pl.show()


def ulozit():
    try:
        x = float(bodx.get())
        y = float(body.get())
        x_ove.append(x)
        y_ove.append(y)
        bodx.set("")
        body.set("")
    except ValueError:
        msb.showerror("Chyba", "Zadejte číslo")


def vyberbarvu():
    global barva
    barva = colorchooser.askcolor()[1]


# proměnné pro souřadnice
bodx = StringVar()
body = StringVar()
x_ove = []
y_ove = []

# Vzhled aplikace
ram = LabelFrame(hlavni, text="Zadání souřadnic", bd=2, relief="ridge", padx=5, pady=5)
ram.pack(padx=10, pady=10)

popis1 = Label(ram, text="Souřadnice x", font="Calibri 10")
popis1.grid(row=0, column=0, pady=3)
vstupx = Entry(ram, font="Calibri 10", textvariable=bodx)
vstupx.grid(row=0, column=1, pady=3)

popis2 = Label(ram, text="Souřadnice y", font="Calibri 10")
popis2.grid(row=1, column=0, pady=3)
vstupy = Entry(ram, font="Calibri 10", textvariable=body)
vstupy.grid(row=1, column=1, pady=3)

uloz = Button(ram, text="Ulož a další", width=15, font="Calibri 12", command=ulozit)
uloz.grid(row=2, column=0, columnspan=2, pady=10)

barva = "black"
barvy = Button(
    hlavni,
    text="Vyber barvu",
    width=15,
    font="Calibri 12 bold",
    command=vyberbarvu,
)
barvy.pack(pady=10)

kresligraf = Button(
    hlavni, text="Vykresli graf", width=15, font="Calibri 12 bold", command=graf
)
kresligraf.pack(pady=10)


hlavni.mainloop()
