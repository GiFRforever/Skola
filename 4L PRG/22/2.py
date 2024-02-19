import tkinter as tk
from datetime import datetime
from random import randint
from time import sleep


class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master: tk.Tk = master
        self.pack(fill=tk.BOTH, expand=1)
        self.clock()

    def clock(self):
        self.hodiny = tk.Canvas(self, width=400, height=200)
        self.čas = self.hodiny.create_text(
            200, 100, text="", font=("Arial", 40, "bold")
        )
        self.hodiny.pack()
        sleep(1 - datetime.now().microsecond / 1000000)  # synchronizace s časem
        self.update()
        self.rainbow()

    def update(self):
        self.hodiny.itemconfigure(self.čas, text=datetime.now().strftime("%H:%M:%S"))
        self.hodiny.after(100, self.update)

    def rainbow(self):
        self.hodiny.configure(bg=f"#{(color := randint(0, 0xFFFFFF)):06X}")
        self.hodiny.itemconfigure(self.čas, fill=f"#{(color^0xFFFFFF):06X}")
        self.after(1000, self.rainbow)


root = tk.Tk()
app = App(root)
app.pack()
root.resizable(False, False)
root.mainloop()
