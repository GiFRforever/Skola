from tkinter import *

hlavni=Tk()



button1=Button(hlavni,width=10,text="Otevřít")
button1.pack(pady=3) 
button2=Button(hlavni,width=10,text="Uložit")
button2.pack(pady=3) 
vyber=Button(hlavni,text="Výběr barvy")
vyber.pack(padx=5,pady=5) 

hlavni.mainloop()
