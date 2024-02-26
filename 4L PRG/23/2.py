import tkinter as tk
from tkinter import messagebox
import urllib.request
import json


class App(tk.Frame):
    def __init__(self, master) -> None:
        super().__init__(master)
        self.master = master
        self.pack(padx=10, pady=10)
        base_currency = "CZK"
        url: str = f"https://open.er-api.com/v6/latest/{base_currency}"
        response = urllib.request.urlopen(url)
        self.data: dict[str, float] = json.loads(response.read().decode())["rates"]
        self.smenarna()

    def smenarna(self) -> None:
        self.vstup = tk.Entry(
            self,
            width=6,
            font=("", 20),
            justify="right",
        )
        self.vstup.grid(
            row=0,
            column=0,
        )
        tk.Label(
            self,
            text="Kč",
            font=("", 20),
        ).grid(row=0, column=1)
        tk.Button(self, text="Převeď", font=("", 17), command=self.vypocet).grid(
            row=0, column=2
        )
        self.vstup.focus_set()
        self.vstup.bind("<Return>", self.vypocet)
        self.option = tk.StringVar(value="EUR")
        tk.Radiobutton(
            self,
            text="EUR",
            variable=self.option,
            value="EUR",
            font=("", 20),
            command=self.__vypocet,
        ).grid(row=1, column=0)
        tk.Radiobutton(
            self,
            text="USD",
            variable=self.option,
            value="USD",
            font=("", 20),
            command=self.__vypocet,
        ).grid(row=1, column=1)
        tk.Radiobutton(
            self,
            text="GBP",
            variable=self.option,
            value="GBP",
            font=("", 20),
            command=self.__vypocet,
        ).grid(row=1, column=2)
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
            self.vystup["text"] = (
                f"{vstup * self.data[self.option.get()]:.02f} {self.option.get()}"
            )
        except ValueError:
            self.vystup["text"] = ""
            if thang:
                raise ValueError


root = tk.Tk()
app = App(root)
root.mainloop()
