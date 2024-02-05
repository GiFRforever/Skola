from logging import root
import tkinter as tk


class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.platno = tk.Canvas(self, width=800, height=800, bg="black")
        self.platno.pack()
        self.kolecko = self.platno.create_oval(100, 100, 200, 200, fill="red")

    def motion(self, event):
        x, y = event.x, event.y
        self.platno.coords(self.kolecko, x - 50, y - 50, x + 50, y + 50)


root = tk.Tk()
app = App(root)
root.title("Hover")
root.bind("<Motion>", app.motion)
app.mainloop()
