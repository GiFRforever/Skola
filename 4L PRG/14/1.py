import tkinter as tk
from turtle import color


class Barvičky(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack(padx=1, pady=1)
        self.configure(bg="#d4d0c8")
        self.default_font = ("Trebuchet MS", 12)
        self.barvičky()

    def barvičky(self):
        self.raml = tk.LabelFrame(self, bg="#d4d0c8", text="Barva pozadí")
        self.raml.grid(row=0, column=0, padx=10, pady=5, sticky="nsew")
        self.ramr = tk.LabelFrame(self, bg="#d4d0c8", text="Barva písma")
        self.ramr.grid(row=0, column=1, padx=10, pady=5, sticky="nsew")

        self.colors: dict[str, tuple[str, str]] = {
            "černá": ("černý", "#000000"),
            "modrá": ("modrý", "#0000ff"),
            "červená": ("červený", "#ff0000"),
            "zelená": ("zelený", "#00ff00"),
            "bílá": ("bílý", "#ffffff"),
        }
        self.pozadí = tk.StringVar()
        self.písmo = tk.StringVar()
        self.pozadí.set("bílá")
        self.písmo.set("černá")
        for c in self.colors.keys():
            tk.Radiobutton(
                self.raml,
                text=c,
                font=self.default_font,
                bg="#d4d0c8",
                value=c,
                variable=self.pozadí,
            ).pack(anchor="w")
            tk.Radiobutton(
                self.ramr,
                text=c,
                font=self.default_font,
                bg="#d4d0c8",
                value=c,
                variable=self.písmo,
            ).pack(anchor="w")

        self.výstup = tk.Label(
            self, text="Černý text", font=self.default_font, bg="white"
        )
        self.výstup.grid(row=1, column=0, sticky="nsew", padx=1, pady=1)

        self.nastavit = tk.Button(
            self, text="Nastavit", font=self.default_font, command=self.změna
        )
        self.nastavit.grid(row=1, column=1, padx=10, pady=1)

    def změna(self):
        self.výstup.configure(
            bg=self.colors[self.pozadí.get()][1],
            fg=self.colors[self.písmo.get()][1],
            text=self.colors[self.písmo.get()][0][:-1].capitalize() + "ý text",
        )


okno = tk.Tk()
okno.title("Barvičky")
okno.resizable(False, False)
app = Barvičky(okno)
app.mainloop()
