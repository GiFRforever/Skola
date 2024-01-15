import tkinter as tk
from tkinter import messagebox as msb

from numpy import pad


class App(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):
        horniMenu = tk.Menu(self.master)
        self.master.config(menu=horniMenu)

        menuText = tk.Menu(horniMenu, tearoff=0)
        text = tk.StringVar(self, "Období")
        menuText.add_radiobutton(label="Jaro", variable=text, value="Jaro")
        menuText.add_radiobutton(label="Léto", variable=text, value="Léto")
        menuText.add_radiobutton(label="Podzim", variable=text, value="Podzim")
        menuText.add_radiobutton(label="Zima", variable=text, value="Zima")
        horniMenu.add_cascade(label="Text", menu=menuText)

        rainbow = tk.Label(
            self.master, textvariable=text, bg="White", font=("Arial", 42)
        )
        rainbow.pack(fill=tk.BOTH, expand=1)

        menuBarva = tk.Menu(horniMenu, tearoff=0)
        barva = tk.StringVar(self, "White")
        prebarvy = lambda: rainbow.config(bg=barva.get())
        menuBarva.add_radiobutton(
            label="Červená", variable=barva, value="Red", command=prebarvy
        )
        menuBarva.add_radiobutton(
            label="Modrá", variable=barva, value="Blue", command=prebarvy
        )
        menuBarva.add_radiobutton(
            label="Zelená", variable=barva, value="Green", command=prebarvy
        )
        menuBarva.add_separator()
        menuBarva.add_radiobutton(
            label="Bílá", variable=barva, value="White", command=prebarvy
        )
        menuBarva.add_radiobutton(
            label="Fialová", variable=barva, value="Purple", command=prebarvy
        )
        horniMenu.add_cascade(label="Barva", menu=menuBarva)

        menuNapověda = tk.Menu(horniMenu, tearoff=0)
        menuNapověda.add_command(
            label="O programu",
            command=lambda: msb.showinfo(
                "O programu", "Zkušební program na menu\nVytvořil: František Člupný"
            ),
        )
        horniMenu.add_cascade(label="Nápověda", menu=menuNapověda)
        horniMenu.add_command(label="Konec", command=self.master.quit)


root = tk.Tk()
root.geometry("300x200")
app = App(root)
root.mainloop()
