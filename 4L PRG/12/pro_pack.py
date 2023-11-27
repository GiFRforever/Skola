import tkinter as tk


def Mocnina(event=None):
    x = float(vstup.get())
    vystup["text"] = str(x**2)
    vstup.select_range(0, tk.END)


hlavni = tk.Tk()
hlavni.minsize(300, 200)

ram = tk.Frame(hlavni, width=100, height=50, relief="sunken", bd=3, padx=10, pady=10)
ram.pack(padx=5, pady=5)

vstup = tk.Entry(ram)
vstup.pack(
    side="left", padx=5, pady=5
)  # side - umístění komponent vedle sebe (zde zleva)
vstup.focus_set()
vstup.bind("<Return>", Mocnina)

vystup = tk.Label(ram, text="výsledek", width=15)
# vystup.place(x=100, y=10)  # umístění komponenty pomocí souřadnic
vystup.pack(side="right", padx=5, pady=5)

vyp = tk.Button(hlavni, text="Druhá mocnina", width=15, command=Mocnina)
vyp.pack(
    fill=tk.X, padx=5, pady=5
)  # anchor=tk.W - zarovnání West, fill=tk.X - vyplnění vodorovně


hlavni.mainloop()
