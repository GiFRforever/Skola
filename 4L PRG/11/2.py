import tkinter as tk


def Mocnina():
    x = float(vstup.get())
    vystup["text"] = str(x**2)
    vstup.select_range(0, tk.END)


hlavni = tk.Tk()
ram = tk.Frame(hlavni, width=100, height=50, relief="sunken", bd=3, padx=10, pady=10)
ram.pack(padx=5, pady=5)
vstup = tk.Entry(ram)
vstup.pack(
    side="left", padx=5, pady=5
)  # side - umístění komponent vedle sebe (zde zleva)
vstup.focus_set()
vystup = tk.Label(ram, text="výsledek", width=15)
vystup.pack(side="left", padx=5, pady=5)
vyp = tk.Button(hlavni, text="Druhá mocnina", width=15, command=Mocnina)
vyp.pack(padx=5, pady=5)
hlavni.mainloop()
