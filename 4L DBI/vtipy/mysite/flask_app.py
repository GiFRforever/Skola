# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template, request, session, send_from_directory
import os
import hashlib
import MySQLdb


app = Flask(__name__)

app.secret_key = (
    "sgbsrtbhji§argvhnilůargvjo§argvopthnilbhiwevjnieVSD§SG JHFBHILSVy§NOŮLŮKYLKHŮSBH§KAJJSDRJKLjkůsgjnklůydlgůjdnbjjfbdfjkůaaserjkasdfkkjadrbgjkkuawbaFUŮB3413541SDFGLKYDBNHaBDFB545FBÁĚŠŽ+ĚČŘÍ+ÉŠÍČTZ+ŠÁÍÉČZŘ)ÚÚ"
)


@app.route("/favicon.ico")
def favicon():
    return send_from_directory(
        os.path.join(app.root_path, "static"),
        "favicon.ico",
        mimetype="image/vnd.microsoft.icon",
    )


@app.route("/")
def index():
    return render_template("index.html")


def mydb():
    return MySQLdb.connect(
        "clu40164v2.mysql.pythonanywhere-services.com",
        "clu40164v2",
        "kočkopes",
        "clu40164v2$default",
    )



@app.route("/prihlaseni-do-systemu/", methods=["GET", "POST"])
def login():
    zprava = ""
    session.pop("uziv", None)  # odhlaseni":
    if request.method == "POST":
        jm = request.form["jmeno"]
        hs = md5(jm + ";;;tajnyobsah;;;" + request.form["heslo"])
        with mydb() as db:
            cur = db.cursor()
            cur.execute("SELECT login,heslo,id FROM uziv WHERE login=%s AND povolen='A';", (jm,))
            udaje = cur.fetchall()
            for udaj in udaje:
                if udaj[1] == hs:
                    session["uziv"] = jm
                    session["id_uziv"] = udaj[2]
                    return render_template(
                        "login.html", uspech="Úspěšně přihlášen jako " + jm
                    )
        zprava = "Chybné přihlášení"
    return render_template("login.html", zprava=zprava)


@app.route("/registrace/", methods=["GET", "POST"])
def registrace():
    chyba = ""
    jmenoform = ""
    if request.method == "POST":
        try:
            jm = request.form["jmeno"]
            hs = request.form["heslo"]
            hs2 = request.form["heslo2"]
            if not all((jm, hs, hs2)):
                chyba = "Uživatelské jméno a heslo nesmí být prázdné"
            elif hs != hs2:
                chyba = "Zadaná hesla nejsou stejná"
            else:
                with mydb() as db:
                    cur = db.cursor()
                    cur.execute("SELECT login FROM uziv WHERE login=%s;", (jm,))
                    udaje = cur.fetchall()
                    if udaje:
                        chyba = f"Uživatelské jméno {jm} je již zabráno"
                    else:
                        cur.execute(
                            "INSERT INTO uziv (login, heslo) VALUES (%s, %s);",
                            (jm, md5(jm + ";;;tajnyobsah;;;" + hs)),
                        )
                        db.commit()
                        return render_template(
                            "login.html",
                            zprava=f"Uzivatel {jm} úspěšně registrován",
                            jmenoform=jm,
                        )
        except:
            chyba = "Chyba parametrů"

    return render_template("registrace.html", chyba=chyba, jmenoform=jmenoform)


def md5(vstup):
    return hashlib.md5(vstup.encode("utf-8")).hexdigest()


@app.route("/sprava_uzivatelu/", methods=["GET", "POST"])
def sprava():
    with mydb() as db:
        cur = db.cursor()
        if request.method == "POST":
            akce = request.form["akce"]
            idcko = request.form["ID"]
            if akce == "Delete":
                cur.execute("DELETE FROM uziv WHERE id=%s;", (idcko,))
            elif akce == "Zakázat":
                cur.execute(
                    "UPDATE uziv SET povolen='N' WHERE id=%s;", (idcko,)
                )
            elif akce == "Povolit":
                cur.execute(
                    "UPDATE uziv SET povolen='A' WHERE id=%s;", (idcko,)
                )

            db.commit()
        cur.execute("SELECT id, login, povolen FROM uziv WHERE login <> 'admin' ORDER BY id ASC;")
        udaje = cur.fetchall()
    return render_template("sprava_uzivatelu.html", udaje=udaje)

@app.route("/vtipy/", methods=["GET", "POST"])
def vtipy():
    with mydb() as db:
        cur = db.cursor()
        cur.execute("SELECT * FROM vtip")
        haha = cur.fetchall()
    return render_template("vtip.html", vtipy=haha)

@app.route("/pridat_vtip/", methods=["GET", "POST"])
def vtip_add():
    zprava = ""
    if request.method == "POST":
        with mydb() as db:
            cur = db.cursor()
            try:
                cur.execute("INSERT INTO vtip (nadpis, obsah, id_uziv) VALUES (%s, %s, %s)", (request.form['nazev'], request.form['ftip'], session["id_uziv"]))
                db.commit()
            except:
                zprava = "Nevyšlo to"
    return render_template("pridat_vtip.html", zprava=zprava)
