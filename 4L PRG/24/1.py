import tkinter as tk


class App(tk.Frame):
    def __init__(self, master) -> None:
        super().__init__(master)
        self.master = master
        self.pack(padx=10, pady=10)
        self.main()

    def main(self) -> None:
        self.table = tk.Frame(self)
        self.table.grid(column=0, row=0, sticky="nsew")
        self.vyber = tk.LabelFrame(self, text="Výběr funkce")
        self.vyber.grid(column=0, row=1, sticky="ns")
        funkce: list[str] = ["x**2", "1/x"]
        for i, f in enumerate(funkce):
            tk.Button(
                self.vyber, text=f, width=10, command=lambda f=f: self.make_table(f)
            ).grid(column=i, row=0, padx=5, pady=5)

    def make_table(self, funkce: str) -> None:
        col_count, row_count = 4, 25
        self.table.destroy()
        self.table = tk.Frame(self)
        self.table.grid(column=0, row=0, sticky="nsew")
        for i in range(col_count * 2):
            self.table.columnconfigure(
                i,
                weight=1,
                minsize=75,
            )

        for i in range(row_count):
            self.table.rowconfigure(i, weight=1, minsize=25)

        for i in range(col_count * 2):
            tk.Label(
                self.table,
                text=funkce if i % 2 else "x",
                background="red",
                relief="raised",
            ).grid(row=0, column=i, sticky="nsew")

        for i in range(1, row_count + 1):
            for j in range(col_count * 2):
                if j % 2:
                    x: int = i + (j // 2) * 25
                    o: int | float = eval(funkce)
                    out: str
                    if isinstance(o, int):
                        out = f"{o:07d}"
                    elif isinstance(o, float):
                        out = f"{o:1.5f}"
                else:
                    out = f"{i + (j // 2) * 25}"
                tk.Label(
                    self.table,
                    text=out,
                    relief="raised",
                ).grid(row=i, column=j, sticky="nsew")


root = tk.Tk()
app = App(root)
root.mainloop()
