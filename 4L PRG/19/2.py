import tkinter as tk
import random as rd


okno = tk.Tk()
okno.title("Tabulka")


for i in range(5):
    for j in range(10):
        entry = tk.Entry(
            okno,
            bg=f"#{rd.randint(0, 0xFFFFFF):06x}",
            font="Arial 18",
            width=5,
        )
        entry.grid(row=j, column=i)
        entry.insert(0, f"{i+1},{j+1}")

okno.mainloop()
