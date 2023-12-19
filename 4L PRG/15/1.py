import tkinter as tk
from random import choice


class App(tk.Frame):
    def __init__(self, master: tk.Tk):
        super().__init__(master)
        self.master = master
        self.pack()

        self.names: list[str] = ["kámen", "nůžky", "papír", "tapír", "Spock"]

        self.bounds: dict[str, tuple[tuple[int, int], tuple[int, int]]] = {
            # nazev: (( x1,  x2), ( y1,  y2)),
            "kámen": ((315, 425), (355, 445)),
            "nůžky": ((195, 310), (50, 135)),
            "papír": ((375, 460), (180, 265)),
            "tapír": ((50, 190), (360, 445)),
            "Spock": ((35, 110), (160, 255)),
        }

        self.rules: dict[str, list[tuple[str, str]]] = {
            # nazev: [(nazev, text), (nazev, text)]
            "kámen": [("nůžky", "tupí"), ("tapíra", "rozdrtí")],
            "nůžky": [("papír", "stříhají"), ("tapírovi", "utnou hlavu")],
            "papír": [("kámen", "balí"), ("Spocka", "usvědčí")],
            "tapír": [("papír", "sní"), ("Spocka", "otráví")],
            "Spock": [("kámen", "vypaří"), ("nůžky", "zničí")],
        }

        self.hra()

    def hra(self) -> None:
        self.canvas = tk.Canvas(self, bg="white", width=500, height=500)
        self.canvas.pack(fill="both", expand=True)
        self.bg = tk.PhotoImage(file="kamen_zde_t.png")
        self.canvas.create_image(False, False, image=self.bg, anchor=tk.NW)
        self.master.bind("<Button-1>", self.click)
        self.master.bind("<Escape>", lambda e: self.master.destroy())
        self.score = (0, 0)
        self.score_text = self.canvas.create_text(
            250,
            470,
            text="{}:{}".format(*self.score),
            font=("Impact", 20),
            fill="white",
            anchor="center",
        )

    def update_score(self, outcome: str) -> None:
        try:
            self.canvas.delete(self.score_text)
        except Exception:
            pass

        if outcome == "win":
            self.score = (self.score[0] + 1, self.score[1])
        elif outcome == "lose":
            self.score = (self.score[0], self.score[1] + 1)
        else:
            return
        self.score_text = self.canvas.create_text(
            250,
            470,
            text="{}:{}".format(*self.score),
            font=("Impact", 20),
            fill="white",
            anchor="center",
        )

    def oponent(self, volba: str):
        protivolba: str = choice(self.names)
        print(f"Oponent: {protivolba}")

        def play_game(self, volba, protivolba):
            """
            Play the game and update the canvas based on the chosen options.

            Args:
                volba (str): The player's choice.
                protivolba (str): The opponent's choice.

            Returns:
                None
            """
            if volba == protivolba:
                print("Remíza!")
                try:
                    self.canvas.delete(self.green_rect)
                    self.canvas.delete(self.red_rect)
                    self.canvas.delete(self.outcome)
                except Exception:
                    pass

                self.outcome = self.canvas.create_text(
                    250,
                    30,
                    text="Remíza",
                    anchor="center",
                    font=("Impact", 20),
                    fill="orange",
                )

                x0, x1 = self.bounds[volba][0]
                y0, y1 = self.bounds[volba][1]

                # create green rectangle
                self.green_rect = self.canvas.create_rectangle(
                    x0, y0, x1, y1, fill="orange"
                )
                self.canvas.tag_lower(self.green_rect)

                x0, x1 = self.bounds[protivolba][0]
                y0, y1 = self.bounds[protivolba][1]
                # create red rectangle
                self.red_rect = self.canvas.create_rectangle(
                    x0, y0, x1, y1, fill="orange"
                )
                self.canvas.tag_lower(self.red_rect)
                return

            for k, v in self.rules.items():
                if k == volba:
                    for i in v:
                        if i[0][:3] == protivolba[:3]:
                            print(f"\33[32mVyhrál jsi! {volba} {i[1]} {i[0]}!\33[0m")

                            try:
                                self.canvas.delete(self.green_rect)
                                self.canvas.delete(self.red_rect)
                                self.canvas.delete(self.outcome)
                            except Exception:
                                pass

                            self.outcome = self.canvas.create_text(
                                250,
                                30,
                                text=f"Vyhrál jsi! {volba} {i[1]} {i[0]}!",
                                anchor="center",
                                font=("Impact", 20),
                                fill="green",
                            )

                            self.update_score("win")

                            x0, x1 = self.bounds[volba][0]
                            y0, y1 = self.bounds[volba][1]

                            # create green rectangle
                            self.green_rect = self.canvas.create_rectangle(
                                x0, y0, x1, y1, fill="green"
                            )
                            self.canvas.tag_lower(self.green_rect)

                            x0, x1 = self.bounds[protivolba][0]
                            y0, y1 = self.bounds[protivolba][1]
                            # create red rectangle
                            self.red_rect = self.canvas.create_rectangle(
                                x0, y0, x1, y1, fill="red"
                            )
                            self.canvas.tag_lower(self.red_rect)
                            return
                if k == protivolba:
                    for i in v:
                        if i[0][:3] == volba[:3]:
                            print(
                                f"\33[91mProhrál jsi! {protivolba} {i[1]} {i[0]}!\33[0m"
                            )

                            try:
                                self.canvas.delete(self.green_rect)
                                self.canvas.delete(self.red_rect)
                                self.canvas.delete(self.outcome)
                            except Exception:
                                pass

                            self.outcome = self.canvas.create_text(
                                250,
                                30,
                                text=f"Prohrál jsi! {protivolba} {i[1]} {i[0]}!",
                                anchor="center",
                                font=("Impact", 20),
                                fill="red",
                            )

                            self.update_score("lose")

                            x0, x1 = self.bounds[protivolba][0]
                            y0, y1 = self.bounds[protivolba][1]

                            # create green rectangle
                            self.green_rect = self.canvas.create_rectangle(
                                x0, y0, x1, y1, fill="green"
                            )
                            self.canvas.tag_lower(self.green_rect)

                            x0, x1 = self.bounds[volba][0]
                            y0, y1 = self.bounds[volba][1]
                            # create red rectangle
                            self.red_rect = self.canvas.create_rectangle(
                                x0, y0, x1, y1, fill="red"
                            )
                            self.canvas.tag_lower(self.red_rect)

                            return

        def click(self, event: tk.Event):
            """
            Handle the click event on the canvas.

            Args:
                event (tk.Event): The click event.

            Returns:
                str: The selected option.
            """
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
            else:
                try:
                    self.canvas.delete(self.green_rect)
                    self.canvas.delete(self.red_rect)
                    self.canvas.delete(self.outcome)
                except Exception:
                    pass

        okno = tk.Tk()
        okno.title("Kámen, nůžky, papír, tapír, spock")
        okno.geometry("500x500")
        okno.resizable(False, False)
        app = App(master=okno)
        app.mainloop()
