import tkinter as tk
import math

root = tk.Tk()
top = tk.Frame(root)
top.pack(side="top")

hwtext = tk.Label(top, text="Hello, World! The sine of")
hwtext.grid(row=0, column=0, sticky="e")

r = tk.StringVar()
r.set("1.2")
r_entry = tk.Entry(top, width=6, textvariable=r)
r_entry.grid(row=1, column=1, sticky="ew")  # sticky "ew" = tk.E + tk.W = tk.EW

s = tk.StringVar()


def comp_s(event):
    global s
    s.set("%g" % math.sin(float(eval(r.get()))))  # construct string


r_entry.bind("<Return>", comp_s)


compute = tk.Label(top, text=" equals ")
compute.grid(row=2, column=2, sticky="w")

s_label = tk.Label(top, textvariable=s, width=18)
s_label.grid(row=1, column=3, sticky="ew")

root.mainloop()
