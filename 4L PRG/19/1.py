import tkinter as tk
import random as rd


canvas = tk.Canvas(width=500, height=500)
canvas.pack()
for i in range(5):
    canvas.create_line(
        *[rd.randint(0, 500) for _ in range(4)],
        fill=f"#{rd.randint(0, 0xFFFFFF):06x}",
        width=3,
    )
canvas.mainloop()
