import tkinter as tk


def Smazat():
    vstup.delete(0, tk.END)  # smaže vše


def Vlozit():
    vstup.insert(
        0, "Něco jiného"
    )  # vkládá na začátek,(END,"text") - na konec (INSERT,"text") - na místo kurzoru


def Oznacit():
    vstup.select_range(0, tk.END)  # označí celý text


def Zobrazit():
    vystup["text"] = vstup.get()  # get()- vrací hodnotu


hlavni = tk.Tk()
vstup = tk.Entry(hlavni, width=20, font="Arial 12", bd=5)  # okraj
vystup = tk.Label(hlavni, text="výstup", font="Arial 15")
akce = tk.LabelFrame(
    hlavni, text="Akce", bd=2, relief="ridge", padx=10, pady=10
)  # padx a pady jsou zde vnitřní vycpávky
akce.pack(padx=5, pady=5)
vystup.pack(padx=5, pady=5)
vstup.pack(padx=5, pady=5)
vstup.focus_set()  # kurzor nastavený v Entry
smazat = tk.Button(akce, text="Smaž", width=10, command=Smazat)
smazat.pack(padx=5, pady=5)
vlozit = tk.Button(akce, text="Vlož", width=10, command=Vlozit)
vlozit.pack(padx=5, pady=5)
oznacit = tk.Button(akce, text="Oznac", width=10, command=Oznacit)
oznacit.pack(padx=5, pady=5)
zobrazit = tk.Button(akce, text="Zobraz", width=10, command=Zobrazit)
zobrazit.pack(padx=5, pady=5)

hlavni.mainloop()
