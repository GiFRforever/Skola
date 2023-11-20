from tkinter import *


def Smazat():
    vstup.delete(0, END)  # smaže vše


def Vlozit():
    vstup.insert(
        0, "Něco jiného"
    )  # vkládá na začátek,(END,"text") - na konec (INSERT,"text") - na místo kurzoru


def Oznacit():
    vstup.select_range(0, END)  # označí celý text


def Zobrazit():
    vystup["text"] = vstup.get()  # get()- vrací hodnotu


hlavni = Tk()
vstup = Entry(hlavni, width=20, font="Arial 12", bd=5)  # okraj
vystup = Label(hlavni, text="výstup", font="Arial 15")
akce = LabelFrame(
    hlavni, text="Akce", bd=2, relief="ridge", padx=10, pady=10
)  # padx a pady jsou zde vnitřní vycpávky
akce.pack(padx=5, pady=5)
vystup.pack(padx=5, pady=5)
vstup.pack(padx=5, pady=5)
vstup.focus_set()  # kurzor nastavený v Entry
smazat = Button(akce, text="Smaž", width=10, command=Smazat)
smazat.pack(padx=5, pady=5)
vlozit = Button(akce, text="Vlož", width=10, command=Vlozit)
vlozit.pack(padx=5, pady=5)
oznacit = Button(akce, text="Oznac", width=10, command=Oznacit)
oznacit.pack(padx=5, pady=5)
zobrazit = Button(akce, text="Zobraz", width=10, command=Zobrazit)
zobrazit.pack(padx=5, pady=5)


hlavni.mainloop()
