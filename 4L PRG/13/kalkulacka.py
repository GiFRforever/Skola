import tkinter as tk
import re

okno = tk.Tk()
okno.title("Kalkulačka")
okno.resizable(False, False)

font = ("Trebuchet Ms", 30)


def validation(action: str):
    # print(action)
    if all(x in [".", ",", "-", "+", "*", "/", "Error"] or x.isdigit() for x in action):
        try:
            if float(action) == int(action):
                brno.insert(0, int(action))
                return False
        except:
            return True
    else:
        return False


brno = tk.Entry(okno, font=font, justify="right")
brno.config(validate="key")
brno.config(validatecommand=(okno.register(validation), "%S"))
brno.register(validation)
brno.grid(row=0, column=0, columnspan=5)
brno.focus_set()


def vstup(znak):
    # / => */+
    # * => */+
    # + => */+-
    # - => */+-
    # , => O,
    if brno.get() == "Error":
        brno.delete(0, tk.END)

    if znak == ".":
        znak = ","

    for _ in range(2):
        if (
            znak in ["*", "/", "+"]
            and brno.get()[-1] in [",", "*", "/", "+", "-"]
            or znak == "-"
            and brno.get()[-1] in ["-", "+"]
        ):
            brno.delete(len(brno.get()) - 1)

    # if znak == ",":  # , => O,
    #     if "," not in (splitted := re.split(r"[\+\-\*\/]", brno.get())[-1]) and splitted == "0":
    #         znak = "0,"
    #     else:
    #         return

    # if znak in [0, "0", "0,"] and "," not in (splitted := re.split(r"[\+\-\*\/]", brno.get())[-1]) and splitted == "0":
    #     return

    brno.insert(len(brno.get()), str(znak))


answer = ""


def pocitej():
    global answer
    try:
        answer = eval(brno.get().replace(",", "."))
        brno.delete(0, tk.END)
        brno.insert(0, answer)
    except:
        brno.delete(0, tk.END)
        brno.insert(0, "Error")


# čisílka
c0 = tk.Button(okno, text=0, font=font, command=lambda: vstup(0))
c1 = tk.Button(okno, text=1, font=font, command=lambda: vstup(1))
c2 = tk.Button(okno, text=2, font=font, command=lambda: vstup(2))
c3 = tk.Button(okno, text=3, font=font, command=lambda: vstup(3))
c4 = tk.Button(okno, text=4, font=font, command=lambda: vstup(4))
c5 = tk.Button(okno, text=5, font=font, command=lambda: vstup(5))
c6 = tk.Button(okno, text=6, font=font, command=lambda: vstup(6))
c7 = tk.Button(okno, text=7, font=font, command=lambda: vstup(7))
c8 = tk.Button(okno, text=8, font=font, command=lambda: vstup(8))
c9 = tk.Button(okno, text=9, font=font, command=lambda: vstup(9))

c0.grid(row=4, column=1, sticky="we")
c1.grid(row=3, column=0, sticky="we")
c2.grid(row=3, column=1, sticky="we")
c3.grid(row=3, column=2, sticky="we")
c4.grid(row=2, column=0, sticky="we")
c5.grid(row=2, column=1, sticky="we")
c6.grid(row=2, column=2, sticky="we")
c7.grid(row=1, column=0, sticky="we")
c8.grid(row=1, column=1, sticky="we")
c9.grid(row=1, column=2, sticky="we")


tecka = tk.Button(okno, text=".", font=font, command=lambda: vstup(","))
tecka.grid(row=4, column=0, sticky="we")

plus = tk.Button(okno, text="+", font=font, command=lambda: vstup("+"))
plus.grid(row=3, column=3, sticky="we")

minus = tk.Button(okno, text="-", font=font, command=lambda: vstup("-"))
minus.grid(row=3, column=4, sticky="we")

krat = tk.Button(okno, text="*", font=font, command=lambda: vstup("*"))
krat.grid(row=2, column=3, sticky="we")

dele = tk.Button(okno, text="/", font=font, command=lambda: vstup("/"))
dele.grid(row=2, column=4, sticky="we")

ans = tk.Button(okno, text="Ans", font=font, command=lambda: vstup(answer))
ans.grid(row=4, column=3, sticky="we")

rovn = tk.Button(okno, text="=", font=font, command=pocitej)
rovn.grid(row=4, column=4, sticky="we")


cs = tk.Button(
    okno, text="CS", font=font, command=lambda: brno.delete(len(brno.get()) - 1)
)
cs.grid(row=1, column=3, sticky="we")

clr = tk.Button(okno, text="CLR", font=font, command=lambda: brno.delete(0, tk.END))
clr.grid(row=1, column=4, sticky="we")


okno.mainloop()
