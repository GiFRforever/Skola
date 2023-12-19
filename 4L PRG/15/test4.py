from tkinter import Canvas, Frame, Tk

from PIL import ImageTk

t = Tk()
t.title("Transparency")

frame = Frame(t)
frame.pack()

canvas = Canvas(frame, bg="black", width=500, height=500)
canvas.pack()

photoimage = ImageTk.PhotoImage(file="kamen_zde_t.png")
canvas.create_rectangle(0, 0, 500, 500, fill="white")
canvas.create_rectangle(0, 0, 250, 250, fill="red")
canvas.create_image(250, 250, image=photoimage)

t.mainloop()
