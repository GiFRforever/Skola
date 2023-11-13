from email.policy import default
import tkinter as tk
import random
from turtle import back


class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()
        self.kalkulacka()

    def kalkulacka(self):
        self.configure(bg="#d4d0c8")
        self.label = tk.Label(
            self,
            text="Výsledek",
            font=("Trebuchet MS", 20),
            fg="white",
            background="black",
            width=20,
            height=3,
        )
        self.label.pack(pady=10, padx=10)

        font_button = ("Trebuchet MS", 15)

        self.sum_button = tk.Button(
            self,
            text="Součet",
            font=font_button,
            width=8,
            height=1,
            background="#d4d0c8",
            relief="raised",
            fg="blue",
            command=self.sum,
        )
        self.sum_button.pack(side="top", pady=10)

        self.sub_button = tk.Button(
            self,
            text="Rozdíl",
            font=font_button,
            width=8,
            height=1,
            background="#d4d0c8",
            relief="raised",
            fg="red",
            command=self.sub,
        )
        self.sub_button.pack(side="top", pady=10)

        self.mul_button = tk.Button(
            self,
            text="Součin",
            font=font_button,
            width=8,
            height=1,
            background="#d4d0c8",
            relief="raised",
            fg="green",
            command=self.mul,
        )
        self.mul_button.pack(side="top", pady=10)

        self.div_button = tk.Button(
            self,
            text="Podíl",
            font=font_button,
            width=8,
            height=1,
            background="#d4d0c8",
            relief="raised",
            fg="yellow",
            command=self.div,
        )
        self.div_button.pack(side="top", pady=10)

        self.quit_button = tk.Button(
            self,
            text="Konec",
            font=font_button,
            width=8,
            height=1,
            background="#d4d0c8",
            relief="raised",
            fg="black",
            command=self.master.destroy,
        )
        self.quit_button.pack(side="bottom", pady=10)

    def sum(self):
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        result = num1 + num2
        self.label["text"] = f"{num1} + {num2} = {result}"
        self.label["fg"] = "blue"

    def sub(self):
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        result = num1 - num2
        self.label["text"] = f"{num1} - {num2} = {result}"
        self.label["fg"] = "red"

    def mul(self):
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        result = num1 * num2
        self.label["text"] = f"{num1} * {num2} = {result}"
        self.label["fg"] = "green"

    def div(self):
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        result = num1 / num2
        self.label["text"] = f"{num1} / {num2} = {result:.2g}"
        self.label["fg"] = "yellow"


okno = tk.Tk()
okno.title("Kalkulačka")
# okno.geometry("326x591")
okno.resizable(False, False)
app = App(master=okno)
app.mainloop()
