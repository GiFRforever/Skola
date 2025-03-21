import random as rd
import tkinter as tk


class App(tk.Frame):
    def __init__(self, master: tk.Tk):
        super().__init__(master)
        self.master = master
        self.pack()
        self.main()

    def main(self) -> None:
        self.pozice = [(rd.uniform(0.1, 0.9), rd.uniform(0.1, 0.9)) for _ in range(8)]
        check = True
        while check:
            check = False
            for i in range(len(self.pozice)):
                for j in range(i + 1, len(self.pozice)):
                    if (
                        self.pozice[i][0] - 0.045
                        < self.pozice[j][0]
                        < self.pozice[i][0] + 0.045
                    ) and (
                        self.pozice[i][1] - 0.089
                        < self.pozice[j][1]
                        < self.pozice[i][1] + 0.089
                    ):
                        self.pozice[j] = (rd.uniform(0, 0.96), rd.uniform(-0.03, 0.9))
                        check = True

        self.kolečka = []
        for souradnice in self.pozice:
            label = tk.Label(
                self.master,
                text="o",
                font=("Arial", 20, "bold"),
                fg="#{:06x}".format(rd.randint(0, 0xFFFFFF)),
                bg="black",
                bd=0,
                highlightthickness=0,
            )
            label.place(relx=souradnice[0], rely=souradnice[1])
            self.kolečka.append(label)
        
        self.update()
        
    def update(self) -> None:
        for i in range(len(self.pozice)):
            self.pozice[i] = (
                self.pozice[i][0] + rd.uniform(-0.01, 0.01),
                self.pozice[i][1] + rd.uniform(-0.01, 0.01),
            )
            self.kolečka[i].place(
                relx=self.pozice[i][0], rely=self.pozice[i][1], anchor="center"
            )
        self.master.after(100, self.update)
        


root = tk.Tk()
root.title("Metoda place")
root.geometry("400x300")
root.resizable(False, False)
root.configure(bg="black")
app = App(root)
root.mainloop()
