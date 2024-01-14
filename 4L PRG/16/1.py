import tkinter as tk
from tkinter import messagebox

from numpy import sign


class App(tk.Frame):
    def __init__(self, master: tk.Tk):
        super().__init__(master)
        self.master = master
        self.pack()
        self.kalkulacka()

    def kalkulacka(self) -> None:
        vcmd = (self.master.register(self.validate), "%W", "%P")
        # print(vcmd)

        self.num1 = tk.IntVar(self)
        self.num1sb = tk.Spinbox(
            self,
            from_=-100,
            to=100,
            textvariable=self.num1,
            validate="key",
            validatecommand=vcmd,
        )
        self.num1sb.pack(padx=10, pady=1)

        self.num2 = tk.IntVar(self)
        self.num2sb = tk.Spinbox(
            self,
            from_=-100,
            to=100,
            textvariable=self.num2,
            validate="key",
            validatecommand=vcmd,
        )
        self.num2sb.pack(padx=10, pady=1)

        self.vystup = tk.Label(self, text="0", font="Arial 20")
        self.vystup.pack(padx=10, pady=10)
        self.vystup.bind(
            "<Button-1>",
            lambda event: (
                self.vystup.config(text=round(float(eval(self.vystup["text"])), 2))
            )
            if isinstance(self.vystup["text"], str)
            else self.vypocet(),
        )

        self.volba = tk.StringVar()
        self.vyber = tk.OptionMenu(self, self.volba, "+", "-", "*", "/")
        self.vyber.pack(padx=10, pady=1)

        self.pocitej = tk.Button(self, text="=", command=self.vypocet)
        self.pocitej.pack(padx=10, pady=10)

        self.master.bind("<Return>", lambda event: self.vypocet())

    def validate(self, caller, value) -> bool:
        try:
            if value in ["", "-"]:  # Allow empty entry and minus sign
                return True

            # print(value)
            # Attempt to convert the entered value to an integer
            int_value = int(value)
            # Check if the integer value is within the specified range
            return -100 <= int_value <= 100

            # if caller == ".!app.!spinbox":
            #     target: tk.IntVar = self.num1
            # elif caller == ".!app.!spinbox2":
            #     target: tk.IntVar = self.num2
            # else:
            #     raise Exception("Unknown widget")
            # if int_value > 100:
            #     target.set(100)
            # elif int_value < -100:
            #     target.set(-100)
            # else:
            #     return True
            # return False
        except ValueError:
            # If the conversion to integer fails, it's not a valid number
            return False
        return False

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
                    jedna, dva = int(self.num1.get()), int(self.num2.get())
                    deleni = jedna / dva
                    znamenko = 1
                    if isinstance(deleni, float):
                        if deleni.is_integer():
                            deleni = int(deleni)
                        elif deleni == round(deleni, 2):
                            pass
                        else:
                            match sign(jedna), sign(dva):
                                case (1, 1):
                                    pass
                                case (-1, -1):
                                    jedna, dva = abs(jedna), abs(dva)
                                case _:
                                    jedna, dva = abs(jedna), abs(dva)
                                    znamenko = -1

                            while True:
                                max_div = min(jedna, dva) ** 0.5
                                for i in range(2, int(max_div) + 1):
                                    if jedna % i == 0 and dva % i == 0:
                                        jedna //= i
                                        dva //= i
                                        break
                                else:
                                    break
                            deleni = f"{znamenko*jedna}/{dva}"

                    self.vystup["text"] = deleni
                else:
                    messagebox.showerror("Chyba", "Nelze dělit nulou!")
        except:
            messagebox.showerror("Chyba", "Něco se pokazilo!")


okno = tk.Tk()
okno.title("Kalkulačka")
okno.resizable(False, False)
app = App(master=okno)
app.mainloop()
