# Menu
from tkinter import *
from tkinter import messagebox as msb

hlavni = Tk()
hlavni.minsize(300, 200)

HorniMenu = Menu(hlavni)  # vytvoření hlavního menu


# jednotlivé položky menu
HorniMenu.add_command(label="Soubor")
HorniMenu.add_command(label="Nastavení")
HorniMenu.add_command(label="Nápověda")
HorniMenu.add_command(label="Konec", command=hlavni.quit)

# říkám, že bude zobrazeno právě HorniMenu
hlavni.config(menu=HorniMenu)

hlavni.mainloop()
