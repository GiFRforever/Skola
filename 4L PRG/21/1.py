import tkinter as tk
from tkinter import filedialog as fd
from tkinter import messagebox as msb

class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master: tk.Tk = master
        self.pack(fill=tk.BOTH, expand=1)
        self.okno()
    
    def okno(self):
        self.filename = ""

        HorniMenu = tk.Menu(self.master)

        menuSoubor = tk.Menu(HorniMenu, tearoff=0)
        menuSoubor.add_command(label="Otevřít", command=self.open)
        menuSoubor.add_command(label="Uložit", command=self.save)
        menuSoubor.add_command(label="Uložit jako", command=self.save_as)
        HorniMenu.add_cascade(label="Soubor", menu=menuSoubor)

        menuText = tk.Menu(HorniMenu, tearoff=0)
        menuText.add_command(label="Nový text", command=self.new)
        HorniMenu.add_cascade(label="Text", menu=menuText)

        HorniMenu.add_command(label="Konec", command=self.quit)


        self.master.config(menu=HorniMenu)

        self.text = tk.Text(self, font="Arial 10")
        self.text.pack(fill=tk.BOTH, expand=1)
    
    def save(self):
        try:
            with open(self.filename, "w") as file:
                file.write(self.text.get(1.0, tk.END))
        except FileNotFoundError:
            msb.showerror("TXT Editor", "Soubor nenalezen.")
    
    def save_as(self):
        self.filename = fd.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Documents", "*.txt")] )
        if self.save():
            msb.showinfo("TXT Editor", "Úspěšně uloženo.")

    def open(self):
        self.filename = fd.askopenfilename(defaultextension=".txt", filetypes=[("Text Documents", "*.txt")] )
        try:
            with open(self.filename, "r") as file:
                self.text.delete(1.0, tk.END)
                self.text.insert(tk.END, file.read())
            # msb.showinfo("App", "Úspěšně uloženo.")
        except FileNotFoundError:
            msb.showerror("TXT Editor", "Soubor nenalezen.")

    def new(self):
        ask = msb.askyesnocancel("TXT Editor", "Uložit soubor?")
        if ask == None:
            return
        elif ask == True:
            if self.filename:
                self.save()
            else:
                self.save_as()
        self.text.delete(1.0, tk.END)

    def quit(self) -> None:
        ask = msb.askyesnocancel("TXT Editor", "Uložit soubor?")
        if ask == None:
            return
        elif ask == True:
            if self.filename:
                self.save()
            else:
                self.save_as()
        return super().quit()

root = tk.Tk()
root.title("TXT Editor")
app = App(root)
root.protocol('WM_DELETE_WINDOW', app.quit)
root.mainloop()
