"""
#Spinbox

from tkinter import *

hlavni=Tk()

cislo = Spinbox(hlavni,from_=-50,to=1000)
cislo.pack(padx=10,pady=10)

vypis = Label(hlavni,text="0",font="Arial 20")
vypis.pack(padx=10,pady=10)


hlavni.mainloop()


#OptionMenu

from tkinter import *


hlavni=Tk()

promenna = StringVar()

vyber = OptionMenu(hlavni,promenna,"jedna","dva","tři")
vyber.pack(padx=10,pady=10)

vystup = Label(hlavni,text="jedna",font="Cambria 12")
vystup.pack(padx=10,pady=10)


hlavni.mainloop()


#OptionMenu - seznam parametrů

from tkinter import *


hlavni=Tk()

parametry = ["první","druhý","třetí"]

promenna = StringVar()

vyber = OptionMenu(hlavni,promenna)
vyber.configure(width=10)
vyber.pack(padx=10,pady=10)

vystup = Label(hlavni,text="jedna",font="Cambria 12")
vystup.pack(padx=10,pady=10)


hlavni.mainloop()

"""

#Příklad kurzovní lístek

from tkinter import *

mena = []

with open("listek.txt") as soubor:
    while True:
        kod = soubor.read(3)
        if kod == "":
            break
        mena.append(kod)
        soubor.readline()

print(mena)

hlavni = Tk()

prom = StringVar()
prom.set(mena[0])


vyber = OptionMenu(hlavni,prom, *mena)
vyber.pack()


hlavni.mainloop()

