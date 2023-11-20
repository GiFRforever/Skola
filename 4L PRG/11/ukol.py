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
        self.pack()
        self.kalkulacka()

    def kalkulacka(self):
        self.configure(bg="#d4d0c8")
        self.default_font = ("Trebuchet MS", 12)
        self.ram = tk.Frame(
            self, width=100, height=50, relief="sunken", bd=3, padx=10, pady=10
        )
        self.ram.pack(padx=5, pady=5)
        self.ram.configure(bg="#d4d0c8")

        self.entry_1 = tk.Entry(self.ram, width=20, font=self.default_font, bd=5)
        self.entry_1.pack(side="left", padx=5, pady=5)
        self.entry_1.focus_set()

        self.output = tk.Label(
            self, text="Výsledek", font=self.default_font, bg="#d4d0c8"
        )
        self.output.pack(padx=5, pady=5)

        self.entry_2 = tk.Entry(self.ram, width=20, font=self.default_font, bd=5)
        self.entry_2.pack(side="right", padx=5, pady=5)

        self.button_sum = tk.Button(
            self.ram, text="+", font=self.default_font, width=2, command=self.sum
        )
        self.button_sum.pack(side="left", padx=5, pady=5)
        self.button_sub = tk.Button(
            self.ram, text="-", font=self.default_font, width=2, command=self.sub
        )
        self.button_sub.pack(side="left", padx=5, pady=5)
        self.button_mul = tk.Button(
            self.ram, text="*", font=self.default_font, width=2, command=self.mul
        )
        self.button_mul.pack(side="left", padx=5, pady=5)
        self.button_div = tk.Button(
            self.ram, text="/", font=self.default_font, width=2, command=self.div
        )
        self.button_div.pack(side="left", padx=5, pady=5)

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
app = Kalkulacka(okno)
app.mainloop()
