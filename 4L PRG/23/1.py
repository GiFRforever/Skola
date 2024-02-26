import tkinter as tk
from tkinter import messagebox


class App(tk.Frame):
    def __init__(self, master) -> None:
        super().__init__(master)
        self.master = master
        self.pack(padx=10, pady=10)
        self.prevodnik()

    def prevodnik(self) -> None:
        self.vstup = tk.Entry(
            self,
            width=8,
            font=("", 20),
            justify="right",
        )  # dl
        self.vstup.grid(row=0, column=0, columnspan=2)
        tk.Label(
            self,
            text="dl",
            font=("", 20),
        ).grid(row=0, column=2)
        self.vstup.focus_set()
        self.vstup.bind("<Return>", self.vypocet)
        self.option = tk.StringVar(value="ml")
        self.option_menu = tk.OptionMenu(
            self, self.option, "ml", "cl", "l", command=self.__vypocet
        )
        self.option_menu.config(font=("", 20))
        self.option_menu.grid(row=1, column=0, columnspan=1)
        self.pocitej = tk.Button(
            self,
            text="Převeď",
            font=("", 17),
            command=self.vypocet,
        )
        self.pocitej.grid(row=1, column=1, columnspan=2)
        self.vystup = tk.Label(
            self,
            font=("", 20),
        )
        self.vystup.grid(row=2, column=0, columnspan=3)

    def vypocet(self, event=None) -> None:
        try:
            self.__vypocet(True)
        except Exception:
            messagebox.showerror("Chyba", "Zadejte číslo")

    def __vypocet(self, thang=None) -> None:
        try:
            vstup = self.vstup.get()
            vstup = vstup.replace(",", ".")
            vstup = float(vstup)
            if vstup < 0:
                messagebox.showerror("Chyba", "Zadejte kladné číslo")
                return
            if self.option.get() == "ml":
                self.vystup["text"] = f"{vstup * 100:.02f} ml"
            elif self.option.get() == "cl":
                self.vystup["text"] = f"{vstup * 10:.02f} cl"
            elif self.option.get() == "l":
                self.vystup["text"] = f"{vstup / 10:.02f} l"
        except ValueError:
            self.vystup["text"] = ""
            if thang:
                raise ValueError


root = tk.Tk()
app = App(root)
app.mainloop()
