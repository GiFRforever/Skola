import tkinter as tk
from tkinter import filedialog as fd
import random as rd

class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master: tk.Tk = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        HorniMenu = tk.Menu(self.master)
        menuSoubor = tk.Menu(HorniMenu, tearoff=0)
        menuSoubor.add_command(label="Otevřít", command=self.save)
        HorniMenu.add_cascade(label="Soubor", menu=menuSoubor)
        self.master.config(menu=HorniMenu)
        self.done = tk.Label(self, text="", font=("Trebuchet Ms", 30))
        self.done.pack(anchor="center")

    
    def save(self):
        filename = fd.askopenfilename(defaultextension=".txt", filetypes=[("Text Documents", "*.txt")] )
        try:
            with open(filename, "w") as file:
                for _ in range(100):
                    file.write(f"#{rd.randint(0, 0xffffff):06x}\n")
            self.done.config(text="Hotovo", fg="green")
        except FileNotFoundError:
            self.done.config(text="Soubor nenalezen", fg="red")
        


root = tk.Tk()
app = App(root)
root.geometry("300x200")
root.mainloop()
