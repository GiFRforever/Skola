from tkinter import *
from tkinter import messagebox as msb

hlavni = Tk()


def Hlaska(a):
    msb.showinfo(a, a + " - není naprogramováno")


# vytvoření hlavního menu
HorniMenu = Menu(hlavni)


# vytvoření jedné rozbalovací nabídky a připojení do hl. menu
menuSoubor = Menu(HorniMenu, tearoff=0)
menuSoubor.add_command(label="Otevřít")
menuSoubor.add_command(label="Uložit")
menuSoubor.add_separator()
# menuSoubor.add_command(label="Konec", command=hlavni.quit)
HorniMenu.add_cascade(label="Soubor", menu=menuSoubor)


# Druhá rozbalovací nabídka
v = IntVar(hlavni, 0)
v1 = IntVar(hlavni, 1)
menuUpravy = Menu(HorniMenu, tearoff=0)
menuUpravy.add_command(label="Vyjmout")
menuUpravy.add_command(label="Kopírovat")
menuUpravy.add_command(label="Vložit")
menuUpravy.add_separator()
menuUpravy.add_checkbutton(label="Pokus", variable=v)
menuUpravy.add_separator()
menuUpravy.add_radiobutton(
    label="První",
    variable=v1,
    value=1,
)
menuUpravy.add_radiobutton(label="Druhý", variable=v1, value=2)
menuUpravy.add_radiobutton(label="Třetí", variable=v1, value=3)
HorniMenu.add_cascade(label="Úpravy", menu=menuUpravy)

# Položky hlavního menu
# HorniMenu.add_command(label="Soubor",command=lambda:Hlaska("Soubor"))
HorniMenu.add_command(label="Nastavení", command=lambda: Hlaska("Nastavení"))
HorniMenu.add_command(label="Nápověda", command=lambda: Hlaska("Nápověda"))
HorniMenu.add_command(label="Konec", command=hlavni.quit)

hlavni.config(menu=HorniMenu)

hlavni.mainloop()
