import tkinter as tk


class Linear(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack(padx=1, pady=1)
        self.linear()

    def linear(self):
        self.configure(bg="#d4d0c8")
        self.default_font = ("Trebuchet MS", 12)
        self.validation = self.register(self.only_numbers)

        self.ram = tk.Frame(self, bg="#d4d0c8")
        self.ram.pack(padx=100, pady=5)

        self.entry_a = tk.Entry(
            self.ram,
            font=self.default_font,
            width=3,
            validate="key",
            validatecommand=(self.validation, "%S"),
        )
        self.entry_a.grid(row=0, column=0, padx=1, pady=5)
        self.label_x = tk.Label(
            self.ram, text="x + ", font=self.default_font, bg="#d4d0c8"
        )

        self.label_x.grid(row=0, column=1)
        self.entry_b = tk.Entry(
            self.ram,
            font=self.default_font,
            width=3,
            validate="key",
            validatecommand=(self.validation, "%S"),
        )
        self.entry_b.grid(row=0, column=2, padx=1, pady=5)
        self.label_0 = tk.Label(
            self.ram, text=" = 0", font=self.default_font, bg="#d4d0c8"
        )

        self.entry_a.focus_set()
        self.entry_a.bind("<Return>", self.solve)
        self.entry_b.bind("<Return>", self.solve)

        self.label_0.grid(row=0, column=3)
        self.button_solve = tk.Button(
            self, text="Vyřešit", font=self.default_font, width=10, command=self.solve
        )

        self.button_solve.pack(pady=10)
        self.output = tk.Label(
            self, text="Výsledek = ", font=self.default_font, bg="#d4d0c8"
        )

        self.output.pack(pady=10)
        self.button_end = tk.Button(
            self, text="Konec", font=self.default_font, width=10, command=self.quit
        )
        self.button_end.pack(pady=10)

    def solve(self, event=None):
        a = float(self.entry_a.get())
        b = float(self.entry_b.get())
        if a == 0:
            self.output["text"] = f"Výsledek neexistuje"
        else:
            self.output["text"] = f"Výsledek = {((-b) / a):.2f}"

    def only_numbers(self, char: str):
        return char.isdigit() | (char == "-")


okno = tk.Tk()
okno.title("Kalkulačka lineární rovnice")
okno.resizable(False, False)
app = Linear(okno)
app.mainloop()
