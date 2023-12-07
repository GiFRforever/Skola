import tkinter as tk
import random as rd


class Count(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack(padx=1, pady=1)
        self.easy_mode = True
        self.on = tk.PhotoImage(file="on.png")
        self.off = tk.PhotoImage(file="off.png")
        self.count()
        self.randomize()

    def count(self):
        self.configure()
        self.default_font = ("Trebuchet MS", 12)
        self.validation = self.register(self.only_numbers)

        self.label_name = tk.Label(self, text="Nauč se sčítat", font=self.default_font)
        self.label_name.pack(pady=10, side="top")

        self.label_difficulty = tk.Label(
            self, text="Easy mode", fg="green", font=self.default_font
        )
        self.label_difficulty.pack(pady=10, anchor="n")
        self.button_difficulty = tk.Button(
            self, image=self.on, bd=0, height=50, command=self.change_difficulty
        )
        self.button_difficulty.pack(padx=10, pady=10, anchor="n")

        self.ram = tk.Frame(self)
        self.ram.pack(padx=10, pady=10)

        self.label_a = tk.Label(self.ram, font=self.default_font)
        self.label_a.grid(row=0, column=0, padx=1, pady=5)

        self.label_plus = tk.Label(self.ram, text=" + ", font=self.default_font)
        self.label_plus.grid(row=0, column=1)

        self.label_b = tk.Label(self.ram, font=self.default_font)
        self.label_b.grid(row=0, column=2, padx=1, pady=5)

        self.label_0 = tk.Label(self.ram, text=" = ", font=self.default_font)
        self.label_0.grid(row=0, column=3)

        self.entry_result = tk.Entry(
            self.ram,
            font=self.default_font,
            width=3,
            validate="key",
            validatecommand=(self.validation, "%S"),
        )
        self.entry_result.grid(row=0, column=4, padx=1, pady=5)
        self.entry_result.focus_set()
        self.entry_result.bind("<Return>", self.check)

        self.button_check = tk.Button(
            self, text="Ověřit", font=self.default_font, width=10, command=self.check
        )
        self.button_check.pack(pady=10)

        self.output = tk.Label(self, text="", font=self.default_font)
        self.output.pack(pady=10)

        self.button_next = tk.Button(
            self, text="Další", font=self.default_font, width=10, command=self.randomize
        )
        self.button_next.pack(pady=10)

        self.button_end = tk.Button(
            self, text="Konec", font=self.default_font, width=10, command=self.quit
        )
        self.button_end.pack(pady=10, side="bottom")

    def change_difficulty(self, event=None):
        if self.easy_mode:
            self.easy_mode = False
            self.label_difficulty.config(text="Hard mode")
            self.label_difficulty.config(fg="red")
            self.button_difficulty.config(image=self.off)
        else:
            self.easy_mode = True
            self.label_difficulty.config(text="Easy mode")
            self.label_difficulty.config(fg="green")
            self.button_difficulty.config(image=self.on)
        self.randomize()

    def check(self, event=None):
        if self.output["text"] == "Výsledek je správně":
            self.randomize()
            return
        if self.entry_result.get() == "":
            self.output["text"] = "Nezadal jsi žádnou hodnotu"
            self.output["fg"] = "red"
            return
        a = int(self.label_a["text"])
        b = int(self.label_b["text"])
        result = int(self.entry_result.get())
        if self.label_plus["text"] == " + " and result == a + b:
            self.output["text"] = "Výsledek je správně"
            self.output["fg"] = "green"
        elif self.label_plus["text"] == " - " and result == a - b:
            self.output["text"] = "Výsledek je správně"
            self.output["fg"] = "green"
        else:
            self.output["text"] = "Výsledek je špatně"
            self.output["fg"] = "red"

    def randomize(self):
        if self.easy_mode:
            self.label_a.config(text=rd.randint(0, 10))
            self.label_b.config(text=rd.randint(0, 10))
        else:
            self.label_a.config(text=(a := rd.randint(0, 1000)))

            if (b := (rd.randint(-100, 100) - a)) < 0:
                self.label_plus.config(text=" - ")
            else:
                self.label_plus.config(text=" + ")
            self.label_b.config(text=abs(b))
        self.output["text"] = ""
        self.entry_result.delete(0, tk.END)
        self.entry_result.focus_set()

    def only_numbers(self, char: str):
        return char.isdigit() | (char == "-")


okno = tk.Tk()
okno.title("Nauč se sčítat")
okno.geometry("200x450")
okno.resizable(False, False)
app = Count(okno)
app.mainloop()
