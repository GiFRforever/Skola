import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import os

# app to synchronize files between two directories
# the user has to choose two directories and the app will synchronize them
# the app will have a button to start the synchronization
# the app will have three modes of synchronization:
# - mirror: the target directory will be the same as the source directory
# - update: the target directory will be updated with the source directory
# - both-way: the target directory will be the same as the source directory and vice versa, conflicts will be resolved by the user


class App(tk.Frame):
    def __init__(self, master) -> None:
        super().__init__(master)
        self.master = master
        self.pack(padx=10, pady=10)
        self.main()

    def main(self) -> None:
        self.foldergrid = tk.Frame(self)
        self.foldergrid.grid(column=0, row=0, sticky="nsew")
        self.foldergrid.columnconfigure(0, weight=1, minsize=75)

        self.sourcebutton = tk.Button(
            self.foldergrid, text="Source", command=self.get_source
        )
        self.sourcebutton.grid(column=0, row=0, padx=5, pady=5)
        self.source = tk.StringVar(value="No source selected")
        self.sourcelabel = tk.Label(self.foldergrid, textvariable=self.source)
        self.sourcelabel.grid(column=1, row=0, padx=5, pady=5)

        self.targetbutton = tk.Button(
            self.foldergrid, text="Target", command=self.get_target
        )
        self.targetbutton.grid(column=0, row=1, padx=5, pady=5)
        self.target = tk.StringVar(value="No target selected")
        self.targetlabel = tk.Label(self.foldergrid, textvariable=self.target)
        self.targetlabel.grid(column=1, row=1, padx=5, pady=5)

        self.syncgrid = tk.Frame(self)
        self.syncgrid.grid(column=0, row=1, sticky="nsew")
        self.syncbutton = tk.Button(
            self.syncgrid, text="Synchronize", command=self.synchronize
        )
        self.syncbutton.grid(column=0, row=0, padx=5, pady=5)
        self.syncgrid.columnconfigure(0, weight=1, minsize=75)
        self.mode = tk.StringVar()
        self.mode.set("mirror")
        self.mirrorbutton = tk.Radiobutton(
            self.syncgrid, text="Mirror", variable=self.mode, value="mirror"
        )
        self.mirrorbutton.grid(column=1, row=0, padx=5, pady=5)
        self.updatebutton = tk.Radiobutton(
            self.syncgrid, text="Update", variable=self.mode, value="update"
        )
        self.bothwaybutton = tk.Radiobutton(
            self.syncgrid, text="Both-way", variable=self.mode, value="both-way"
        )
        self.bothwaybutton.grid(column=2, row=0, padx=5, pady=5)

        sourceframe = tk.LabelFrame(self, text="Source")
        sourceframe.grid(column=0, row=2, sticky="nsew")
        sourceframe.columnconfigure(0, weight=1, minsize=75)
        self.sourcetree = ttk.Treeview(sourceframe)

    def get_source(self) -> None:
        new: str = filedialog.askdirectory()
        if new:
            self.source.set(new)
            print(self.source.get())

    def get_target(self) -> None:
        new: str = filedialog.askdirectory()
        if new:
            self.target.set(new)
            print(self.target.get())

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

    def mirrormode(self) -> None:
        print("Mirror mode")

    def updatemode(self) -> None:
        print("Update mode")

    def bothwaymode(self) -> None:
        print("Both-way mode")


root = tk.Tk()
app = App(root)
root.mainloop()
