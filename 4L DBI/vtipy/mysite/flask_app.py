from flask import Flask, url_for, request, render_template, session, redirect
import sqlite3
import hashlib

app = Flask(__name__)

app.secret_key = "hvndasjklfhndasjlf_FAKT_HODNE_TAJNE_hdasjklfhdasjklfhdaf"

# hesla vvvv
# admin: admin
# uzivatel: heslo


@app.route("/", methods=["GET", "POST"])
def index():
    chyba = ""
    with mydb() as db:
        cur = db.cursor()
        if request.method == "POST":
            if request.form.get("akce") == "smazat" and session.get("uziv") == "admin":
                id = request.form["id"]
                cur.execute("DELETE FROM vtip WHERE id=(?)", (id,))

        cur.execute(
            "SELECT id, nazev, COUNT(id_kateg) FROM kateg LEFT JOIN zarazeni ON zarazeni.id_kateg=kateg.id GROUP BY id "
        )
        nazvy = cur.fetchall()
        try:
            if "kateg" in request.form:
                id_kateg = request.form["kateg"]
            else:
                id_kateg = 0
            cur.execute(
                "SELECT nadpis, obsah, vtip.id, vtip.id_uziv FROM vtip,zarazeni WHERE zarazeni.id_vtip = vtip.id AND zarazeni.id_kateg = ?",
                (id_kateg,),
            )
        except Exception as e:
            cur.execute("SELECT nadpis, obsah, vtip.id, vtip.id_uziv FROM vtip")
            chyba = e
        vtipy = cur.fetchall()

    if session.get("uziv"):
        cur.execute(
            "SELECT COUNT(id) FROM vtip WHERE id_uziv = ?", (session.get("id_uziv"),)
        )
        count_uziv = cur.fetchone()
    else:
        count_uziv = None

    cur.execute("SELECT COUNT(id) FROM vtip")
    count = cur.fetchone()

    return render_template(
        "index.html",
        nazvy=nazvy,
        vtipy=vtipy,
        chyba=chyba,
        count=count,
        count_uziv=count_uziv,
    )


def md5(vstup):
    return hashlib.md5(vstup.encode("utf-8")).hexdigest()


def mydb():
    # return MySQLdb.connect("uziv123.mysql.pythonanywhere-services.com", "uziv123", "asdfghjkl2", "uziv123$default")
    db = sqlite3.connect("dbvtipy.sqlite3")
    db.execute("PRAGMA foreign_keys=ON")
    return db


@app.route("/pridat_vtip/", methods=["GET", "POST"])
def pridat_vtip():
    chyba = ""
    data = {"nadpis": "", "obsah": ""}
    with mydb() as db:
        cur = db.cursor()
        cur.execute("SELECT id, nazev FROM kateg")
        nazvy = cur.fetchall()
        nazvy.pop(0)
    if request.method == "POST":
        # try:
        data = request.form
        nadpis = data["nadpis"]
        obsah = data["obsah"]
        with mydb() as db:
            cur = db.cursor()
            cur.execute(
                "INSERT INTO vtip (nadpis,obsah,id_uziv) VALUES (?,?,?)",
                (nadpis, obsah, session["id_uziv"]),
            )
            db.commit()
            cur.execute(
                "SELECT id FROM vtip where nadpis=? and obsah=? and id_uziv=?",
                (nadpis, obsah, session["id_uziv"]),
            )
            id_vtip = cur.fetchone()[0]
            cur.execute(
                "INSERT INTO zarazeni (id_vtip,id_kateg) VALUES (?,?)", (id_vtip, 0)
            )
            for kat in nazvy:
                if f"kateg{kat[0]}" in data:
                    cur.execute(
                        "INSERT INTO zarazeni (id_vtip,id_kateg) VALUES (?,?)",
                        (id_vtip, kat[0]),
                    )
            db.commit()
        return redirect(url_for("index"))
        # except Exception as e:
        #     chyba=f"Velký špatný! {e}; {data}"
    return render_template("pridat_vtip.html", chyba=chyba, data=data, nazvy=nazvy)


@app.route("/edit_vtip/", methods=["POST"])
def edit_vtip():
    chyba = ""
    id_vtip = request.form.get("id")
    akce = request.form.get("akce")

    with mydb() as db:
        cur = db.cursor()
        cur.execute("SELECT id, nazev FROM kateg")
        nazvy = cur.fetchall()
        nazvy.pop(0)

        if akce == "Upravit":
            nadpis = request.form.get("nadpis")
            obsah = request.form.get("obsah")
            if all((nadpis, obsah)):
                cur.execute(
                    "UPDATE vtip SET nadpis=?, obsah=? WHERE id=?",
                    (nadpis, obsah, id_vtip),
                )
                db.commit()
                cur.execute("DELETE FROM zarazeni WHERE id_vtip=?", (id_vtip,))
                cur.execute(
                    "INSERT INTO zarazeni (id_vtip,id_kateg) VALUES (?,?)",
                    (id_vtip, 0),
                )
                for kat in nazvy:
                    if f"kateg{kat[0]}" in request.form:
                        cur.execute(
                            "INSERT INTO zarazeni (id_vtip,id_kateg) VALUES (?,?)",
                            (id_vtip, kat[0]),
                        )
                db.commit()
                return redirect(url_for("index"))
            else:
                chyba = "Není vyplněný nadpis nebo obsah"

        cur.execute("SELECT nadpis, obsah FROM vtip WHERE id=?", (id_vtip,))
        d = cur.fetchone()
        data = {
            "id": id_vtip,
            "nadpis": d[0],
            "obsah": d[1],
        }

        cur.execute("SELECT id_kateg FROM zarazeni WHERE id_vtip=?", (id_vtip,))
        zarazeni = [z[0] for z in cur.fetchall()]

    return render_template(
        "editace.html",
        chyba=chyba,
        data=data,
        nazvy=nazvy,
        zarazeni=zarazeni,
        id_vtip=id_vtip,
    )


@app.route("/login/", methods=["GET", "POST"])
def login():
    zprava = ""
    session.pop("uziv", None)  # odhlaseni":
    if request.method == "POST":
        jm = request.form["jmeno"]
        hs = md5(jm + ";;;tajnyobsah;;;" + request.form["heslo"])

        db = mydb()
        cur = db.cursor()
        cur.execute(
            "SELECT id,login,heslo FROM uziv WHERE login=? and heslo=?;", (jm, hs)
        )
        pocet = cur.fetchone()
        if pocet:
            session["uziv"] = jm
            session["id_uziv"] = pocet[0]
            return redirect("/")
            # return render_template("login.html", uspech="Úspěšně přihlášen jako "+jm)

        zprava = "Chybné přihlášení"
    return render_template("login.html", zprava=zprava)


@app.route("/db/")
def db():
    db = sqlite3.connect("dbvtipy.sqlite3")
    cur = db.cursor()
    cur.execute("SELECT * FROM uziv")
    pocet = cur.rowcount
    rd = cur.fetchall()
    db.close
    return f"jede nám to,pocet={pocet}, rd={rd}"


@app.route("/add/")
def add():
    db = sqlite3.connect("dbvtipy.sqlite3")
    cur = db.cursor()
    cur.execute("INSERT INTO uziv (login,heslo) VAlues (?,?)", ("lojza", "tajneheslo"))
    db.commit()
    db.close
    return f"do tabulky uziv pribyl novy radek"


@app.route("/registrace/", methods=["GET", "POST"])
def registrace():
    chyba = ""
    jmenoform = ""
    if request.method == "POST":
        try:
            jm = request.form["jmeno"]
            hs = request.form["heslo"]
            hs2 = request.form["heslo2"]

            # if jm=="" or hs=="":
            if not all((jm, hs, hs2)):
                chyba = "Uživatelské jméno a heslo nesmí být prázdné"

            elif hs != hs2:
                chyba = "Zadaná hesla nejsou stejná"

            else:

                with mydb() as db:
                    cur = db.cursor()
                    cur.execute("SELECT login FROM uziv WHERE login=?;", (jm,))
                    udaje = cur.fetchone()
                    if udaje:
                        chyba = f"Uživatelské jméno {jm} je již zabráno u={udaje}"
                    else:
                        cur.execute(
                            "INSERT INTO uziv (login, heslo) VALUES (?, ?);",
                            (jm, md5(jm + ";;;tajnyobsah;;;" + hs)),
                        )
                        db.commit()
                        return render_template(
                            "login.html",
                            zprava=f"Uzivatel {jm} úspěšně registrován",
                            jmenoform=jm,
                        )

                """
                with open("uziv.txt", "r") as soubor:
                    radky = soubor.readlines()

                for radek in radky:
                    x=radek.split(";")
                    if len(x)>1:
                        if x[0]==jm:
                            chyba=f"Uživatelské jméno {jm} je již zabráno"
                            break


                if chyba=="":
                    with open("uziv.txt", "a+") as soubor:
                        soubor.write(jm+";"+md5(jm+";;;tajnyobsah;;;"+hs)+";\n" )
                    return render_template("login.html", zprava=f"Uzivatel {jm} úspěšně registrován", jmenoform=jm)
                """

        except:
            chyba = "Chyba parametrů"

    return render_template("registrace.html", chyba=chyba, jmenoform=jmenoform)


"""
create table uziv (id int primary key auto_increment, login varchar(20) not null, heslo varchar(32), jmeno varchar(40), email varchar(40), povolen char(1));
create table vtip (id int primary key auto_increment, nadpis varchar(30), obsah text, id_uziv int, vlozen datetime);
create table zarazen (id_vtipu int, id_kateg int, primary key(id_vtipu,id_kateg));
create table kateg (id int primary key auto_increment, nazev varchar(20));
"""
