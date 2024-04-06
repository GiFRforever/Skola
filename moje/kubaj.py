import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from tkinter import messagebox as msb
import os

# app to synchronize files between two directories
# the user has to choose two directories and the app will synchronize them
# the app will have a button to start the synchronization
# the app will have three modes of synchronization:
# - mirror: the target directory will be the same as the source directory
# - update: the target directory will be updated with the source directory
# - both-way: the target directory will be the same as the source directory and vice versa, conflicts will be resolved by the user


class App(tk.Frame):
    def __init__(self, master: tk.Tk) -> None:
        super().__init__(master)
        self.master: tk.Tk = master
        self.pack(padx=10, pady=10, fill="both", expand=True)
        self.main()

    def main(self) -> None:
        self.mainmenu = tk.Menu(self.master)
        self.mainmenu.add_cascade(label="Nápověda", command=self.showhelp)
        self.mainmenu.add_cascade(label="Konec", command=self.master.quit)
        self.master.config(menu=self.mainmenu)

        self.foldergrid = tk.Frame(self)
        # self.foldergrid.grid(column=0, row=0, sticky="nsw")
        self.foldergrid.pack(anchor="nw", fill="both", expand=True)
        # self.foldergrid.columnconfigure(0, weight=1, minsize=75)

        self.sourcebutton = tk.Button(
            self.foldergrid, text="Source", command=self.get_source
        )
        self.sourcebutton.grid(column=0, row=0, padx=5, pady=5, sticky="nsew")

        self.source = tk.StringVar(value="No source selected")
        self.sourcelabel = tk.Label(self.foldergrid, textvariable=self.source)
        self.sourcelabel.grid(column=1, row=0, padx=5, pady=5)

        self.targetbutton = tk.Button(
            self.foldergrid, text="Target", command=self.get_target
        )
        self.targetbutton.grid(column=0, row=1, padx=5, pady=5, sticky="nsew")

        self.target = tk.StringVar(value="No target selected")
        self.targetlabel = tk.Label(self.foldergrid, textvariable=self.target)
        self.targetlabel.grid(column=1, row=1, padx=5, pady=5)

        self.syncgrid = tk.Frame(self)
        # self.syncgrid.grid(column=0, row=1, sticky="nsw")
        self.syncgrid.pack(anchor="nw", fill="both", expand=True)
        self.syncbutton = tk.Button(
            self.syncgrid, text="Synchronize", command=self.synchronize
        )
        self.syncbutton.grid(column=0, row=0, padx=5, pady=5, sticky="nsew")
        # self.syncgrid.columnconfigure(0, weight=1, minsize=75)
        self.mode = tk.StringVar()
        self.mode.set("mirror")
        self.mirrorbutton = tk.Radiobutton(
            self.syncgrid,
            text="Mirror",
            variable=self.mode,
            value="mirror",
        )
        self.mirrorbutton.grid(column=1, row=0, padx=5, pady=5)
        self.updatebutton = tk.Radiobutton(
            self.syncgrid,
            text="Update",
            variable=self.mode,
            value="update",
        )
        self.updatebutton.grid(column=2, row=0, padx=5, pady=5)
        self.bothwaybutton = tk.Radiobutton(
            self.syncgrid,
            text="Both-way",
            variable=self.mode,
            value="both-way",
        )
        self.bothwaybutton.grid(column=3, row=0, padx=5, pady=5)

        self.dirframe = tk.Frame(self)
        # self.dirframe.grid(column=0, row=2, columnspan=2, sticky="nsew")
        self.dirframe.pack(anchor="nw", fill="both", expand=True)
        # self.dirframe.columnconfigure(0, weight=1, minsize=75)
        self.sourceframe = tk.LabelFrame(self.dirframe, text="Source")
        self.sourceframe.grid(column=0, row=0, sticky="nsew")
        self.targetframe = tk.LabelFrame(self.dirframe, text="Target")
        self.targetframe.grid(column=1, row=0, sticky="nsew")

    def get_source(self) -> None:
        new: str = filedialog.askdirectory()
        if new:
            self.source.set(new)
            print(self.source.get())
        self.sourcetree = DirTree(self.sourceframe, self.source.get())

    def get_target(self) -> None:
        new: str = filedialog.askdirectory()
        if new:
            self.target.set(new)
            print(self.target.get())
        self.targettree = DirTree(self.targetframe, self.target.get())

    def synchronize(self) -> None:
        print(self.mode.get())
        print(self.source.get())
        print(self.target.get())
        if os.path.exists(self.source.get()) and os.path.exists(self.target.get()):
            if self.mode.get() == "mirror":
                self.mirrormode()
            elif self.mode.get() == "update":
                self.updatemode()
            elif self.mode.get() == "both-way":
                self.bothwaymode()
        else:
            print("Source or target does not exist")

    def showhelp(self) -> None:
        msb.showinfo(
            "Nápověda",
            """
Tato aplikace synchronizuje složky třemi způsoby.
- Mirror: Cílová složka bude stejná jako zdrojová složka.
- Update: Cílová složka bude aktualizována zdrojovou složkou.
- Both-way: Cílová složka bude stejná jako zdrojová složka a naopak
Konflikty budou řešeny podle data poslední změny.
            """,
        )

    def mirrormode(self) -> None:
        print("Mirror mode")
        os.system(f'robocopy "{self.source.get()}" "{self.target.get()}" /PURGE /E')

    def updatemode(self) -> None:
        print("Update mode")
        os.system(f'robocopy "{self.source.get()}" "{self.target.get()}" /E /XO')

    def bothwaymode(self) -> None:
        print("Both-way mode")
        os.system(f'robocopy "{self.source.get()}" "{self.target.get()}" /E /XO')
        os.system(f'robocopy "{self.target.get()}" "{self.source.get()}" /E /XO')


class DirTree(object):
    def __init__(self, frame: tk.Frame | tk.LabelFrame, path):
        self.nodes = dict()
        self.frame: tk.Frame | tk.LabelFrame = frame
        self.tree = ttk.Treeview(self.frame)
        ysb = ttk.Scrollbar(self.frame, orient="vertical", command=self.tree.yview)
        xsb = ttk.Scrollbar(self.frame, orient="horizontal", command=self.tree.xview)
        self.tree.configure(yscrollcommand=ysb.set, xscrollcommand=xsb.set)
        self.tree.heading("#0", text="Project tree", anchor="w")

        self.tree.grid()
        ysb.grid(row=0, column=1, sticky="ns")
        xsb.grid(row=1, column=0, sticky="ew")
        self.frame.grid()

        abspath = os.path.abspath(path)
        self.insert_node("", abspath, abspath)
        self.tree.bind("<<TreeviewOpen>>", self.open_node)

    def insert_node(self, parent, text, abspath):
        node = self.tree.insert(parent, "end", text=text, open=False)
        if os.path.isdir(abspath):
            self.nodes[node] = abspath
            self.tree.insert(node, "end")

    def open_node(self, event):
        node = self.tree.focus()
        abspath = self.nodes.pop(node, None)
        if abspath:
            self.tree.delete(*self.tree.get_children(node))
            for p in os.listdir(abspath):
                self.insert_node(node, p, os.path.join(abspath, p))


root = tk.Tk()
app = App(root)
root.title("Zrcadlo")
root.resizable(False, False)
root.mainloop()
