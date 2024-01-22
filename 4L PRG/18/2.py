import tkinter as tk
import re

okno = tk.Tk()
okno.title("Kalkulačka")
okno.resizable(False, False)

font = ("Trebuchet Ms", 30)


brno = tk.Entry(okno, font=font)
brno.grid(row=0, column=0, columnspan=4)
brno.focus_set()

cisilka = [
    (0, 4, 1),
    (1, 3, 0),
    (2, 3, 1),
    (3, 3, 2),
    (4, 2, 0),
    (5, 2, 1),
    (6, 2, 2),
    (7, 1, 0),
    (8, 1, 1),
    (9, 1, 2),
    ("*", 4, 0),
    ("#", 4, 2),
]

for cislo, r, c in cisilka:
    tk.Button(
        okno,
        text=cislo,
        font=font,
        command=lambda cislo=cislo: brno.insert(len(brno.get()), cislo),
    ).grid(row=r, column=c, sticky="we")


cs = tk.Button(okno, text="Smaž", font=font, command=lambda: brno.delete(0, tk.END))
cs.grid(row=5, column=0, columnspan=3, sticky="we")

konec = tk.Button(okno, text="Konec", font=font, command=quit)
konec.grid(row=1, column=3, rowspan=5, sticky="nswe")


okno.mainloop()
