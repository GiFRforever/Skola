from tkinter import *

hlavni = Tk()

info = Button(hlavni,text="Informace",font="Calibri 12 bold",width=15,height=3)
info.grid()

zprava = Button(hlavni,text="Zpráva",font="Calibri 12 bold",width=15,height=3)
zprava.grid(row=1)

dotaz = Button(hlavni,text="Dotaz",font="Calibri 12 bold",width=15,height=3)
dotaz.grid(row=0,column=1)

konec = Button(hlavni,text="Konec",font="Calibri 12 bold",width=15,height=3)
konec.grid(row=1,column=1)



hlavni.mainloop()