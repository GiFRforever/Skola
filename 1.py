import tkinter as tk
import random


class ButtonGame:
    def __init__(self):
        # okno
        self.root = tk.Tk()
        self.root.geometry("400x400")
        self.root.title("Button Game")
        self.root.resizable(False, False)

        # Seznam tlačítek
        self.list_tlacitek: list[tk.Button] = []

        # prvotní umístění tlačítek
        self.umistit_tlacitko()
        self.umistit_tlacitko()
        self.umistit_tlacitko()

        # tlačítko prohodit
        self.mixer = tk.Button(
            self.root, text="Prohodit", command=self.presunout_tlacitka
        )
        self.mixer.place(x=0, y=0)

        # start
        self.root.mainloop()

    def umistit_tlacitko(self):
        # random pozice
        x = random.randint(0, 360)
        y = random.randint(0, 380)
        print(f"Umístění tlačítka: {x}, {y}")
        # vytvoření tlačítka
        tlacitko = tk.Button(
            self.root, text="Konec", bg="red", fg="white", command=self.root.quit
        )

        # přidání tlačítka do seznamu
        self.list_tlacitek.append(tlacitko)

        # umístění tlačítka
        tlacitko.place(x=x, y=y)

    def presunout_tlacitka(self):
        # odstranění tlačítek
        for tlacitko in self.list_tlacitek:
            tlacitko.place_forget()

        # nové umístění tlačítek
        self.umistit_tlacitko()
        self.umistit_tlacitko()
        self.umistit_tlacitko()


# Vytvoření instance třídy ButtonGame
hra = ButtonGame()
