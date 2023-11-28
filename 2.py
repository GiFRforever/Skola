import tkinter as tk


def validate_numbers(func):
    def wrapper(self):
        try:
            float(self.entry_1.get())
            float(self.entry_2.get())
        except ValueError:
            self.output["text"] = "Zadejte prosím čísla!"
        else:
            func(self)

    return wrapper


class Kalkulacka(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack(padx=5, pady=5)
        self.kalkulacka()

    def kalkulacka(self):
        self.configure(bg="#d4d0c8")
        self.default_font = ("Trebuchet MS", 12)
        self.label_1 = tk.Label(
            self, text="Číslo 1:", font=self.default_font, bg="#d4d0c8"
        )
        self.label_1.grid(row=0, column=0, padx=50)
        self.entry_1 = tk.Entry(self, font=self.default_font)
        self.entry_1.grid(row=0, column=1, padx=10, pady=5)
        self.label_2 = tk.Label(
            self, text="Číslo 2:", font=self.default_font, bg="#d4d0c8"
        )
        self.label_2.grid(row=1, column=0)
        self.entry_2 = tk.Entry(self, font=self.default_font)
        self.entry_2.grid(row=1, column=1, padx=10, pady=5)

        self.ram_b = tk.Frame(self, bg="#d4d0c8")
        self.ram_b.grid(row=2, column=0, columnspan=2, pady=10)

        self.button_sum = tk.Button(
            self.ram_b, text="Součet", font=self.default_font, command=self.sum
        )
        self.button_sum.grid(row=0, column=0, sticky="we", padx=10, pady=10)
        self.button_mul = tk.Button(
            self.ram_b, text="Součin", font=self.default_font, command=self.mul
        )
        self.button_mul.grid(row=0, column=1, sticky="we", padx=10, pady=10)
        self.button_sub = tk.Button(
            self.ram_b, text="Rozdíl", font=self.default_font, command=self.sub
        )
        self.button_sub.grid(row=1, column=0, sticky="we", padx=10, pady=10)
        self.button_div = tk.Button(
            self.ram_b, text="Podíl", font=self.default_font, command=self.div
        )
        self.button_div.grid(row=1, column=1, sticky="we", padx=10, pady=10)

        self.output = tk.Label(
            self, text="Výsledek = ", font=self.default_font, bg="#d4d0c8"
        )
        self.output.grid(row=4, column=0, columnspan=2)

    @validate_numbers
    def sum(self):
        x = float(self.entry_1.get())
        y = float(self.entry_2.get())
        self.output["text"] = f"Výsledek = {x + y}"

    @validate_numbers
    def sub(self):
        x = float(self.entry_1.get())
        y = float(self.entry_2.get())
        self.output["text"] = f"Výsledek = {x - y}"

    @validate_numbers
    def mul(self):
        x = float(self.entry_1.get())
        y = float(self.entry_2.get())
        self.output["text"] = f"Výsledek = {x * y}"

    @validate_numbers
    def div(self):
        x = float(self.entry_1.get())
        y = float(self.entry_2.get())
        if y == 0:
            self.output["text"] = "Nelze dělit nulou!"
        else:
            self.output["text"] = f"Výsledek = {x/y}"


okno = tk.Tk()
okno.title("Kalkulačka")
okno.resizable(False, False)
app = Kalkulacka(okno)
app.mainloop()
