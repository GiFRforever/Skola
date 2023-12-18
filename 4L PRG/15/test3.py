import tkinter
import random

c=tkinter.Canvas()
c.pack()
c.config(width=600, height=600)

gw=26
gs=2
go="white"
gf="gray"
rf='green'

for i in range(gs,600, 30):
    for j in range(gs,600, 30):
        c.create_rectangle(i,j,i+gw,j+gw, width=gs, outline=go, fill=gf)

#this is the code for three green squares
for i in range(3):
    rx=random.randrange(gs, 600, 30)
    ry=random.randrange(gs, 600, 30)
    c.create_rectangle(rx, ry, rx+gw, ry+gw, width=gs, fill=rf, outline=go)

c.mainloop()