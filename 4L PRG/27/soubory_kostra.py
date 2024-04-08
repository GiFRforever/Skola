import tkinter as tk
from tkinter import messagebox as msb
from tkinter import filedialog as fld
from tkinter import simpledialog as sdb

hlavni = tk.Tk()


def otevrit() -> None:
    cesta: str = fld.askopenfilename()
    if cesta:
        with open(cesta, "r") as soubor:
            obsah: str = soubor.read()
            text.delete(1.0, tk.END)
            text.insert(tk.END, obsah)


def ulozit() -> None:
    cesta: str = fld.asksaveasfilename()
    if cesta:
        with open(cesta, "w") as soubor:
            soubor.write(text.get(1.0, tk.END))


def velka_pismena() -> None:
    text.insert(tk.END, text.get(1.0, tk.END).upper())


# display messagebox and ask for a character to replace
def nahradit_znak() -> None:
    znak: str | None = sdb.askstring(
        "Nahradit znak", "Zadejte znak, který chcete nahradit"
    )
    if znak:
        nahrazeni: str | None = sdb.askstring(
            "Nahradit znak", f"Zadejte znak, na který chcete znak '{znak}' nahradit"
        )
        if nahrazeni:
            obsah: str = text.get(1.0, tk.END)
            obsah = obsah.replace(znak, nahrazeni)
            text.delete(1.0, tk.END)
            text.insert(tk.END, obsah)


def statistika_znaku() -> None:
    obsah: str = text.get(1.0, tk.END).lower()
    statistika: dict[str, int] = {znak: obsah.count(znak) for znak in abeceda}
    msb.showinfo(
        "Statistika znaků",
        "\n".join(f"{znak}:\t{pocet}" for znak, pocet in statistika.items()),
    )


# pro statistiku
abeceda = "abcdefghijklmnopqrstuvwxyz"

# vzhled aplikace
text = tk.Text(hlavni, font="Arial 10")
text.pack()

hornimenu = tk.Menu(hlavni)

menusoubor = tk.Menu(hornimenu, tearoff=0)
menusoubor.add_command(label="Otevřít", command=otevrit)
menusoubor.add_command(label="Uložit", command=ulozit)
menusoubor.add_separator()
menusoubor.add_command(label="Konec", command=hlavni.quit)
hornimenu.add_cascade(label="Soubor", menu=menusoubor)

menuoperace = tk.Menu(hornimenu, tearoff=0)
menuoperace.add_command(label="Velká písmena", command=velka_pismena)
menuoperace.add_command(label="Nahradit znak", command=nahradit_znak)
menuoperace.add_command(label="Statistika znaků", command=statistika_znaku)
hornimenu.add_cascade(label="Operace", menu=menuoperace)

hlavni.config(menu=hornimenu)

hlavni.mainloop()
