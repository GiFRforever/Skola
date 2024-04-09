from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageTk

import os

os.chdir(r"H:\mujgit\Skola\moje\opiceprojekt")

dokument = Image.open("dokument.png")
graf_ikona = Image.open("graf.png")
odejit = Image.open("odejit.png")
poslat = Image.open("poslat.png")
uzivatel_ikona = Image.open("uzivatel.png")
admin_ikona = Image.open("Admin.png")

urcene_jmeno = "Pepa"
urcene_heslo = "12345"
seznam_uzivatelu = []
pohlavi_pocet = []
oblibene_barvy_graf = []
vek_pocet = []
hlavni_okno = Tk()
hlavni_okno.resizable(False, False)
hlavni_okno.title("Formulář")


def odeslat():
    global seznam_uzivatelu
    global pohlavi_pocet
    global oblibene_barvy_graf
    global vek_pocet
    jmeno = jmeno_entry.get()
    prijmeni = prijmeni_entry.get()
    email = email_entry.get()
    vek = vek_spinbox.get()
    if jmeno and prijmeni and email and vek:
        messagebox.showinfo(
            "Dotazník vyplněn", "Dotazník byl správně vyplněn a odeslán, Děkujeme!"
        )

        pohlavi_text = ""
        if pohlavi.get() == 1:
            pohlavi_text = "Muž"
            pohlavi_pocet.append("Muž")
        elif pohlavi.get() == 2:
            pohlavi_text = "Žena"
            pohlavi_pocet.append("Žena")
        elif pohlavi.get() == 3:
            pohlavi_text = "Jiné"
            pohlavi_pocet.append("Jiné")

        vek_pocet.append(vek)

        oblibene_barvy = []
        if zelena_var.get():
            oblibene_barvy.append("Zelená")
            oblibene_barvy_graf.append("Zelená")
        if cervena_var.get():
            oblibene_barvy.append("Červená")
            oblibene_barvy_graf.append("Červená")
        if modra_var.get():
            oblibene_barvy.append("Modrá")
            oblibene_barvy_graf.append("Modrá")
        jmeno_entry.delete(0, END)
        prijmeni_entry.delete(0, END)
        email_entry.delete(0, END)
        try:
            modra_check_button.deselect()
        except:
            pass
        try:
            zelena_checkbutton.deselect()
        except:
            pass
        try:
            cervena_check_button.deselect()
        except:
            pass
        pohlavi.set(None)

        vek_spinbox.delete(0, END)
        vek_spinbox.insert(0, 5)

        seznam_uzivatelu.append(
            f"Jméno: {jmeno}, Příjmení: {prijmeni}, email: {email}, Pohlaví: {pohlavi_text}, Věk: {vek}"
        )
    else:
        messagebox.showerror(
            "Dotazník špatně vyplněn", "Některé z hodnot nejsou vyplněny"
        )


tab = ttk.Notebook(hlavni_okno)
uzivatel = Frame(tab)
admin = Frame(tab)
hlavni_okno.iconphoto(False, PhotoImage(file="formular.png"))

uzivatel_ik = uzivatel_ikona.resize((40, 30))
uzivatel_novy = ImageTk.PhotoImage(uzivatel_ik)

admin_ik = admin_ikona.resize((40, 30))
admin_novy = ImageTk.PhotoImage(admin_ik)

uzivatel.grid(columnspan=6, rowspan=6)
tab.add(uzivatel, text="Uživatel", image=uzivatel_novy)

admin.grid(columnspan=6, rowspan=6)
tab.add(admin, image=admin_novy)


tab.grid(rowspan=4, columnspan=2)


jmeno_frame = LabelFrame(uzivatel, text="Jméno")
jmeno_frame.grid(row=0, column=0, sticky="NSWE", padx=3)

jmeno_entry = Entry(jmeno_frame)
jmeno_entry.grid(column=0, row=0)


prijmeni_frame = LabelFrame(uzivatel, text="Příjmení")
prijmeni_frame.grid(row=1, column=0, sticky="NSWE", padx=3)

prijmeni_entry = Entry(prijmeni_frame)
prijmeni_entry.grid(column=0, row=0)


email_frame = LabelFrame(uzivatel, text="E-mail")
email_frame.grid(row=2, column=0, sticky="NSWE", padx=3)

email_entry = Entry(email_frame)
email_entry.grid(column=0, row=0)

radiobutton_frame = LabelFrame(uzivatel, text="Pohlaví")
radiobutton_frame.grid(row=0, column=1, rowspan=2, sticky="NSWE", padx=3)


pohlavi = IntVar()
muz_radio = Radiobutton(radiobutton_frame, text="Muž", value=1, variable=pohlavi)
muz_radio.grid(column=0, row=0, sticky="W")
zena_radio = Radiobutton(radiobutton_frame, text="Žena", value=2, variable=pohlavi)
zena_radio.grid(column=0, row=1, sticky="W")
jine_radio = Radiobutton(radiobutton_frame, text="Jiné", value=3, variable=pohlavi)
jine_radio.grid(column=0, row=2, sticky="W")


vek_frame = LabelFrame(uzivatel, text="věk")
vek_frame.grid(row=3, column=0, sticky="NS", padx=3)

vek_spinbox = Spinbox(vek_frame, from_=5, to=100)
vek_spinbox.grid(column=0, row=0)

barvy = LabelFrame(uzivatel, text="Oblíbené barvy")
barvy.grid(row=2, column=1, rowspan=2, sticky="NS", padx=3)

zelena_var = IntVar()
zelena_checkbutton = Checkbutton(barvy, text="Zelená", variable=zelena_var)
zelena_checkbutton.grid(column=0, row=0, sticky="W")
cervena_var = IntVar()
cervena_check_button = Checkbutton(barvy, text="Červená", variable=cervena_var)
cervena_check_button.grid(column=0, row=1, sticky="W")
modra_var = IntVar()
modra_check_button = Checkbutton(barvy, text="Modrá", variable=modra_var)
modra_check_button.grid(column=0, row=2, sticky="W")

upraveny_odeslat = poslat.resize((20, 20))
novy_odeslat = ImageTk.PhotoImage(upraveny_odeslat)

upraveny_odejit = odejit.resize((20, 20))
novy_odejit = ImageTk.PhotoImage(upraveny_odejit)

tlc1 = Button(uzivatel, image=novy_odeslat, command=odeslat)
tlc1.grid(row=4, column=0, sticky="WE", padx=3)
tlc2 = Button(uzivatel, image=novy_odejit, command=exit)
tlc2.grid(row=4, column=1, sticky="WE", padx=3)

# -------------------------------------------------------------------------------------------------------------------------------


def tisk():
    uziv_jmeno = Uziv_jmeno_entry.get()
    heslo = heslo_entry.get()

    if uziv_jmeno == urcene_jmeno and heslo == urcene_heslo:
        messagebox.showinfo("Správné zadané údaje", "Soubor se Vám uložil do vypis.txt")
        soubor = open("vypis.txt", "a", encoding="utf-8")
        for zapis in seznam_uzivatelu:
            soubor.write(f"{zapis}\n")
        soubor.close()
    else:
        messagebox.showerror(
            "Špatně zadané údaje", "Údaje jsou neplatné, prosím zadejte je znovu"
        )

    seznam_uzivatelu.clear()


def graf():
    uziv_jmeno = Uziv_jmeno_entry.get()
    heslo = heslo_entry.get()
    global pohlavi_pocet
    global oblibene_barvy_graf
    global vek_pocet
    print(pohlavi_pocet)
    print(vek_pocet)
    radek = 0
    muz_statistika = []
    zena_statistika = []
    jine_statistika = []
    muzi_celkove = 0
    zeny_celkove = 0
    jine_celkove = 0
    zeny_prumerny_vek = 0
    muz_prumerny_vek = 0
    jine_prumerny_vek = 0
    for pohlavi in pohlavi_pocet:
        if pohlavi == "Muž":
            muz_statistika.append(vek_pocet[radek])
            muzi_celkove = muzi_celkove + int(vek_pocet[radek])
        if pohlavi == "Žena":
            zena_statistika.append(vek_pocet[radek])
            zeny_celkove = zeny_celkove + int(vek_pocet[radek])
        if pohlavi == "Jiné":
            jine_statistika.append(vek_pocet[radek])
            jine_celkove = jine_celkove + int(vek_pocet[radek])
        radek = radek + 1
    try:
        muz_prumerny_vek = muzi_celkove / len(muz_statistika)
    except:
        pass
    try:
        zeny_prumerny_vek = zeny_celkove / len(zena_statistika)
    except:
        pass
    try:
        jine_prumerny_vek = jine_celkove / len(jine_statistika)
    except:
        pass
    if uziv_jmeno == urcene_jmeno and heslo == urcene_heslo:
        data = {
            "Ženy": zeny_prumerny_vek,
            "Muži": muz_prumerny_vek,
            "Jiné": jine_prumerny_vek,
        }
        klice = list(data.keys())
        hodnoty = list(data.values())
        plt.locator_params(axis="y", nbins=10)
        plt.bar(klice, hodnoty, color="black")
        plt.xlabel("Pohlaví")
        plt.ylabel("Průměrný věk")
        plt.title("Průměrný věk jednotlivých pohlaví")
        plt.show()
    else:
        messagebox.showerror(
            "Špatně zadané údaje", "Údaje jsou neplatné, prosím zadejte je znovu"
        )


jmeno_label = LabelFrame(admin, text="Uživatelské jméno")
jmeno_label.pack(fill=X)
Uziv_jmeno_entry = Entry(jmeno_label)
Uziv_jmeno_entry.pack(fill=X)


heslo_label = LabelFrame(admin, text="Heslo")
heslo_label.pack(fill=X)
heslo_entry = Entry(heslo_label)
heslo_entry.pack(fill=X)
upraveny_graf = graf_ikona.resize((20, 20))
novy_graf = ImageTk.PhotoImage(upraveny_graf)

upraveny_dokument = dokument.resize((20, 20))
novy_dokument = ImageTk.PhotoImage(upraveny_dokument)


tl_frame = LabelFrame(admin)
tl_frame.pack(fill=X)
button_tisk = Button(tl_frame, image=novy_dokument, command=tisk, width=115)
button_tisk.grid(column=0, row=0)

button_graf = Button(tl_frame, image=novy_graf, command=graf, width=115)
button_graf.grid(column=1, row=0)


hlavni_okno.mainloop()
