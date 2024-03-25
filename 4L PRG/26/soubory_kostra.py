from tkinter import *
from tkinter import messagebox as msb
from tkinter import filedialog as  fld

hlavni=Tk()

#pro statistiku
abeceda="abcdefghijklmnopqrstuvwxyz"

#vzhled aplikace
text=Text(hlavni,font="Arial 10")
text.pack()

hornimenu=Menu(hlavni)

menusoubor=Menu(hornimenu,tearoff=0)
menusoubor.add_command(label="Otevřít")
menusoubor.add_command(label="Uložit")
menusoubor.add_separator()
menusoubor.add_command(label="Konec")
hornimenu.add_cascade(label="Soubor",menu=menusoubor)

menuoperace=Menu(hornimenu,tearoff=0)
menuoperace.add_command(label="Velká písmena")
menuoperace.add_command(label="Nahradit znak")
menuoperace.add_command(label="Statistika znaků")
hornimenu.add_cascade(label="Operace",menu=menuoperace)

hlavni.config(menu=hornimenu)




hlavni.mainloop()
