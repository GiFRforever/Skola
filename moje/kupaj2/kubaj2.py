import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
import mysql.connector
import os

from mysql.connector.abstracts import MySQLConnectionAbstract, MySQLCursorAbstract
from mysql.connector.pooling import PooledMySQLConnection

# os.chdir(r"H:\mujgit\Skola\moje\kupaj2")
os.chdir(r"/home/clu40164@spseol.cz/wnet_H/mujgit/Skola/moje/kupaj2")


def mydb() -> PooledMySQLConnection | MySQLConnectionAbstract:
    url = "sql11.freesqldatabase.com"
    user = "sql11700285"
    password = "BPstwddWlF"
    port = 3306

    mydb: PooledMySQLConnection | MySQLConnectionAbstract = mysql.connector.connect(
        host=url, user=user, password=password, port=port
    )
    mydb.cursor().execute(f"USE {user}")

    return mydb


# kraje = [
#     "Hlavní město Praha",
#     "Jihočeský kraj",
#     "Jihomoravský kraj",
#     "Karlovarský kraj",
#     "Královehradecký kraj",
#     "Liberecký kraj",
#     "Moravskoslezský kraj",
#     "Olomoucký kraj",
#     "Pardubický kraj",
#     "Plzeňský kraj",
#     "Středočeský kraj",
#     "Ústecký kraj",
#     "Vysočina",
#     "Zlínský kraj",
# ]
# with mydb() as db:
#     c = db.cursor()
#     c.execute("DELETE FROM kraje")
#     for i, kraj in enumerate(kraje):
#         c.execute(f"INSERT INTO kraje (id, nazev) VALUES ({i}, '{kraj}')")
#     db.commit()
#     c.execute("SELECT * FROM kraje")
#     print(c.fetchall())

# exit()

with mydb() as db:
    c = db.cursor()
    c.execute("SELECT id, nazev FROM kraje")
    kraje: dict[int, str] = {id: nazev for id, nazev in c.fetchall()}  # type: ignore věřte mi, že to funguje

# print(kraje)
# exit()


class Form(tk.Frame):
    def __init__(self, frame: tk.Frame):
        super().__init__(frame)
        self.pack()
        self.dotaznik()

    def dotaznik(self):
        self.velikost_label = tk.Label(self, text="Velikost trenek")
        self.velikost_label.pack()
        self.velikost = tk.StringVar()
        self.velikost.set("M")
        self.velikost_combobox = tk.OptionMenu(
            self, self.velikost, "XS", "S", "M", "L", "XL"
        )
        self.velikost_combobox.pack()
        self.vek_label = tk.Label(self, text="Věk")
        self.vek_label.pack()
        self.vek_spinbox = tk.Spinbox(self, from_=18, to=80)
        self.vek_spinbox.config(validate="key")
        self.vek_spinbox.config(
            validatecommand=(self.register(lambda x: x.isdigit()), "%P")
        )
        self.vek_spinbox.pack(padx=10)
        self.kraj_label = tk.Label(self, text="Kraj")
        self.kraj_label.pack()
        self.kraj = tk.StringVar()
        self.kraj.set("Středočeský kraj")
        self.kraj_combobox = tk.OptionMenu(self, self.kraj, *kraje.values())
        self.kraj_combobox.pack()
        self.pohlavi_label = tk.Label(self, text="Pohlaví")
        self.pohlavi_label.pack()
        self.pohlavi = tk.IntVar()
        self.muz = tk.Radiobutton(self, text="Muž", variable=self.pohlavi, value=1)
        self.muz.pack()
        self.zena = tk.Radiobutton(self, text="Žena", variable=self.pohlavi, value=2)
        self.zena.pack()
        self.jine = tk.Radiobutton(self, text="Jiné", variable=self.pohlavi, value=3)
        self.jine.pack()
        self.odeslat_button = tk.Button(self, text="Odeslat", command=self.odeslat)
        self.odeslat_button.pack()

    def odeslat(self):
        try:
            if int(self.vek_spinbox.get()) < 18:
                raise ValueError("Věk musí být větší než 18")
            # odešle data do databáze
            with mydb() as db:
                c = db.cursor()
                c.execute(
                    "CREATE TABLE IF NOT EXISTS dotaznik (id INT AUTO_INCREMENT PRIMARY KEY, velikost VARCHAR(2), vek INT, pohlavi INT, kraj INT, CONSTRAINT kraj FOREIGN KEY (kraj) REFERENCES kraje(id))"
                )
                c.execute(
                    f"INSERT INTO dotaznik (velikost, vek, pohlavi, kraj) VALUES ('{self.velikost.get()}', {self.vek_spinbox.get()}, {self.pohlavi.get()}, {list(kraje.keys())[list(kraje.values()).index(self.kraj.get())]})"
                )
                db.commit()

            mb.showinfo("Úspěch", "Data byla úspěšně odeslána")
        except ValueError as e:
            mb.showerror("Chyba", str(e))
            return


class Graph(tk.Frame):
    def __init__(self, frame: tk.Frame):
        super().__init__(frame)
        self.pack()
        self.graph()

    def graph(self):
        with mydb() as db:
            c: MySQLCursorAbstract = db.cursor()
            c.execute(
                "SELECT kraj, pohlavi, velikost, COUNT(*) FROM dotaznik GROUP BY kraj, pohlavi, velikost"
            )
            dotaznik = c.fetchall()


class Data(tk.Frame):
    def __init__(self, frame: tk.Frame):
        super().__init__(frame)
        self.pack()
        self.data()

    def data(self):
        pass


root = tk.Tk()
root.resizable(False, False)
root.title("Dotazník")

main_panel = ttk.Notebook(root)

formframe = tk.Frame(main_panel)
form = Form(formframe)
main_panel.add(formframe, text="Dotazník")
main_panel.pack()

graphframe = tk.Frame(main_panel)
graph = Graph(graphframe)
graph.pack()
main_panel.add(graphframe, text="Graf")

dataframe = tk.Frame(main_panel)
data = Data(dataframe)
data.pack()
main_panel.add(dataframe, text="Data")

root.mainloop()
