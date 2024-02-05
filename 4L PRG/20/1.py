import tkinter as tk
import random as rd

class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.pack()
        self.okno()
    
    def okno(self):
        self.platno = tk.Canvas(self, width=800, height=800, bg="black")
        self.platno.pack()

    def disko(self, event):
        self.platno['bg'] = f"#{rd.randint(0, 0xffffff):06x}"
    
    def belitko(self, event):
        self.platno['bg'] = "white"

root = tk.Tk()
app = App(root)
root.title("Barvičky")
root.bind("<Button-3>", app.disko)
root.bind("<Button-1>", app.belitko)
root.mainloop()