import tkinter as tk
from random import randint


class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master: tk.Tk = master
        self.pack(fill=tk.BOTH, expand=1)
        self.rainbow()

    def rainbow(self):
        self.configure(bg=f"#{randint(0, 0xFFFFFF):06X}")
        self.after(1000, self.rainbow)


root = tk.Tk()
app = App(root)
app.pack()
root.geometry("300x300")
root.mainloop()
