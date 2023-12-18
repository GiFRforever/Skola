from calendar import c
import tkinter as tk
from random import choice


def diff(a: tuple[int, int]) -> tuple[int, int]:
    return a[1] - a[0]


class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()

        self.names: list[str] = ["kámen", "nůžky", "papír", "tapír", "spock"]

        self.bounds: dict[str, tuple[tuple[int, int], tuple[int, int]]] = {
            # nazev: (( x1,  x2), ( y1,  y2)),
            "kámen": ((315, 425), (360, 445)),
            "nůžky": ((195, 310), (50, 130)),
            "papír": ((375, 460), (180, 265)),
            "tapír": ((50, 190), (360, 445)),
            "spock": ((35, 105), (160, 250)),
        }

        self.rules: dict[str, list[tuple[str, str]]] = {
            "kámen": [("nůžky", "tupí"), ("tapíra", "rozdrtí")],
            "nůžky": [("papír", "stříhají"), ("tapírovi", "utnou hlavu")],
            "papír": [("kámen", "balí"), ("spocka", "usvědčí")],
            "tapír": [("papír", "sní"), ("spocka", "otráví")],
            "spock": [("kámen", "vypaří"), ("nůžky", "zničí")],
        }

        self.hra()

    def hra(self):
        # self.canvas = tk.Canvas(self, width=500, height=500)
        # self.canvas.pack(fill="both", expand=True)
        # self.bg = tk.PhotoImage(file="kamen_zde_t.png")
        # self.canvas.create_image(False, False, image=self.bg, anchor=tk.NW)
        self.master.bind("<Button-1>", self.click)
        self.master.bind("<Escape>", lambda e: self.master.destroy())

    def oponent(self, volba: str):
        protivolba: str = choice(self.names)
        print(f"Oponent: {protivolba}")

        if volba == protivolba:
            print("Remíza!")
            return

        for k, v in self.rules.items():
            if k == volba:
                for i in v:
                    if i[0][:3] == protivolba[:3]:
                        print(f"Vyhrál jsi! {volba} {i[1]} {i[0]}!")
                        x0, x1 = self.bounds[volba][0]
                        y0, y1 = self.bounds[volba][1]
                        # print(x0, x1, y0, y1)

                        #create greeen rectangle
                        self.canvas_g = tk.Canvas(
                            self,
                            width=x1-x0,
                            height=y1-y0,
                        )
                        self.canvas_g.pack(fill="both", expand=True)
                        self.canvas_g.create_rectangle(
                            x0, y0, x1, y1, fill="green"
                        )

                        return
            if k == protivolba:
                for i in v:
                    if i[0][:3] == volba[:3]:
                        print(f"Prohrál jsi! {protivolba} {i[1]} {i[0]}!")
                        return

    def click(self, event: tk.Event):
        # print(f"x: {event.x}, y: {event.y}")
        for k, v in self.bounds.items():
            if (
                event.x >= v[0][0]
                and event.x <= v[0][1]
                and event.y >= v[1][0]
                and event.y <= v[1][1]
            ):
                print(f"TY: {k}!")
                self.oponent(k)
                return k


okno = tk.Tk()
okno.title("Kámen, nůžky, papír, tapír, spock")
okno.geometry("500x500")
okno.resizable(False, False)
app = App(master=okno)
app.mainloop()
