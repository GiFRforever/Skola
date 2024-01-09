import tkinter as tk
from tkinter import messagebox

class App(tk.Frame):
    def __init__(self, master: tk.Tk):
        super().__init__(master)
        self.master = master
        self.pack()
        self.kalkulacka()
    
    def kalkulacka(self) -> None:
        self.num1 = tk.Spinbox(self, from_=-100, to=100)
        self.num1.pack(padx=10, pady=10)

        self.num2 = tk.Spinbox(self, from_=-100, to=100)
        self.num2.pack(padx=10, pady=10)

        self.vystup = tk.Label(self, text="0", font="Arial 20")
        self.vystup.pack(padx=10, pady=10)

        self.volba = tk.StringVar()
        self.vyber = tk.OptionMenu(self, self.volba, "+", "-", "*", "/")
        self.vyber.pack(padx=10, pady=10)

        self.vypocet = tk.Button(self, text="=", command=self.vypocet)
        self.vypocet.pack(padx=10, pady=10)

    def vypocet(self) -> None:
        try:
            if self.volba.get() == "+":
                self.vystup["text"] = int(self.num1.get()) + int(self.num2.get())
            elif self.volba.get() == "-":
                self.vystup["text"] = int(self.num1.get()) - int(self.num2.get())
            elif self.volba.get() == "*":
                self.vystup["text"] = int(self.num1.get()) * int(self.num2.get())
            elif self.volba.get() == "/":
                if int(self.num2.get()) != 0:
                    self.vystup["text"] = int(self.num1.get()) / int(self.num2.get())
                else:
                    messagebox.showerror("Chyba", "Nelze dělit nulou!")
        except:
            messagebox.showerror("Chyba", "Něco se pokazilo!")

okno = tk.Tk()
okno.title("Kalkulačka")
okno.resizable(False, False)
app = App(master=okno)
app.mainloop()

