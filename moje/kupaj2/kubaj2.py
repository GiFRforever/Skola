import tkinter as tk
from tkinter import ttk

import os

os.chdir(r"H:\mujgit\Skola\moje\kupaj2")


class Form(tk.Frame):
    def __init__(self, frame: tk.Frame):
        super().__init__(frame)
        self.pack()
        self.dotaznik()

    def dotaznik(self):
        self.velikost_label = tk.Label(self, text="Velikost trenek")
        self.velikost_label.pack()
        self.velikost = tk.StringVar()
        self.velikost.set("M")
        self.velikost_combobox = tk.OptionMenu(
            self, self.velikost, "XS", "S", "M", "L", "XL"
        )
        self.velikost_combobox.pack()
        self.vek_label = tk.Label(self, text="Věk")
        self.vek_label.pack()
        self.vek_spinbox = tk.Spinbox(self, from_=18, to=80)
        self.vek_spinbox.config(validate="key")
        self.vek_spinbox.config(
            validatecommand=(self.register(lambda x: x.isdigit()), "%P")
        )
        self.vek_spinbox.pack(padx=10)
        self.pohlavi_label = tk.Label(self, text="Pohlaví")
        self.pohlavi_label.pack()
        self.pohlavi = tk.IntVar()
        self.muz = tk.Radiobutton(self, text="Muž", variable=self.pohlavi, value=1)
        self.muz.pack()
        self.zena = tk.Radiobutton(self, text="Žena", variable=self.pohlavi, value=2)
        self.zena.pack()
        self.jine = tk.Radiobutton(self, text="Jiné", variable=self.pohlavi, value=3)
        self.jine.pack()
        self.odeslat_button = tk.Button(self, text="Odeslat", command=self.odeslat)
        self.odeslat_button.pack()

    def odeslat(self):
        pass


class Graph(tk.Frame):
    def __init__(self, frame: tk.Frame):
        super().__init__(frame)
        self.pack()
        self.graph()

    def graph(self):
        pass


root = tk.Tk()
root.resizable(False, False)
root.title("Dotazník")
main_panel = ttk.Notebook(root)
formframe = tk.Frame(main_panel)
form = Form(formframe)
main_panel.add(formframe, text="Dotazník")
main_panel.pack()

graphframe = tk.Frame(main_panel)
graph = Graph(graphframe)
graph.pack()
main_panel.add(graphframe, text="Graf")

root.mainloop()
