import sys, time, os, math as mt

tělesa: list[str] = [
    "_exit_",
    "krychle",
    "kvádr",
    "hranol",
    "jehlan",
    "kužel",
    "válec",
    "koule",
    "torus",
    "*komolá tělesa",
    "*pravidelné mnohostěny",
]

komolá_tělesa: list[str] = [
    "_zpět_",
    "komolý jehlan",
    "komolý kužel",
]

mnohostěny: list[str] = [
    "_zpět_",
    "čtyřstěn",
    "osmistěn",
    "dvanáctistěn",
    "dvacetistěn",
]

koule: list[str] = [
    "                              ",
    "             ....             ",
    "       :~!7????77!!~^:.       ",
    "    .!J555555YYJ??77!!~^:     ",
    "   ~YPPGBBBGGP5YJJ?77!~~~^.   ",
    "  !55PGB#&&#BGP5YJ?77!!~~^^.  ",
    " .JY5PGGBBBBGP5\033[95m|–––––––––––|  r\033[0m",
    " .?JYY55PPP55YYJJ?77!!~~^^^:  ",
    "  ^???JJJJJJJJ??77!!~~^^^^^.  ",
    "   ^!7777777777!!!~~^^^^^:.   ",
    "    .:~!!!!!!~~~~^^^^^^:.     ",
    "       .::^^^^^^^::::.        ",
    "                              ",
]

kvádr: list[str] = [
    "",
    "    .:...............................:^ ",
    "  .:.:                              :.^ ",
    " ^:..^............................::  : ",
    ".:  .:                            :   : ",
    " :   :                            :   :  \033[93mc\033[0m",
    " :   :                            :   : ",
    " :   :                            :   : ",
    " :   :                            :.  :.",
    " :  ::............................^..:^ ",
    " ^.:                              :.:.  \033[93mb\033[0m",
    " ^:...............................:.    ",
    "                 \033[93ma\033[0m                       ",
]
# hranol: list[str] = kvádr

jehlan: list[str] = [
    "                   \033[93m–\033[0m                   ",
    "                  :\033[93m|\033[0m:                  ",
    "                 .?\033[93m|\033[0mJ.                 ",
    "                .!^\033[93m|\033[0m~~^                ",
    "               .~^ \033[93m|\033[0m:^:^               ",
    "               ~:: \033[93m|\033[0m ! .~.             ",
    "              ~.^  \033[93m|\033[0m ^: .~:            ",
    "             ~.:.  \033[93m|\033[0m .~   ^^           ",
    "            ~. ^   \033[93m|\033[0m  ~.   :^          ",
    "           ~. :.   \033[93m|\033[0m  :~    .~.        ",
    "          ~. .^    \033[93m|\033[0m   !.    .~:       ",
    "         ~.  :.    \033[93m| h\033[0m ^^      ^^      ",
    "        ~:  .:     \033[93m|\033[0m    !       :^     ",
    "       ~:   ^      \033[93m|\033[0m    ^:       .~.   ",
    "      ~:   .:      \033[93m|\033[0m    .~         ~.  ",
    "     ~:   .~:... : \033[93m|\033[0m:... !.: .... . 7~ ",
    "    ~:  .:         \033[93m|\033[0m     :~      .^^^. ",
    "   ^: .:           \033[93m–\033[0m      ~    .:^.    ",
    "  ^^.:                   ^^ :^:.      ",
    " \033[93m!7:::::::::::::::::::::::7^:\033[0m         ",
    "              \033[93ma\033[0m                       ",
]

komolý_jehlan: list[str] = [
    "",
    "             ,,,,:::\033[93m=\033[0m^^^^^^^^::         ",
    "         ::::,,,,^,,\033[93m|\033[0m,~...::'''.^.       ",
    "        :^      :.  \033[93m|\033[0m :^         ^:      ",
    "       :^      ..   \033[93m|\033[0m  ~.         :^     ",
    "      ^^      .:    \033[93m|\033[0m  .~          .^.   ",
    "     ^:       :     \033[93m|\033[0m   ^:           ^:  ",
    "    ^:       :      \033[93m| h\033[0m  ~            :^ ",
    "   ^:       :.......\033[93m|\033[0m.. .:~ . . . . . .^!",
    "  ^.    ...         \033[93m|\033[0m     ^:      ..:::'",
    " ^.  . .            \033[93m–\033[0m     ~   ..:::'    ",
    "\033[93m7^:::.....................^~:\033[0m::'        ",
    "              \033[93ma\033[0m                         ",
]

krychle: list[str] = [
    "",
    "    .:..................:^ ",
    "  .:.:                 :.^ ",
    " ^:..^...............::  : ",
    ".:  .:               :   : ",
    " :   :               :   :  \033[93ma\033[0m",
    " :   :               :   : ",
    " :   :               :   : ",
    " :   :               :   :",
    " :  ::...............:...: ",
    " ^.:                 : .'  \033[93ma\033[0m",
    " ^:..................:'    ",
    "            \033[93ma\033[0m               ",
]

kužel: list[str] = [
    "",
    "                          \033[96m::\033[0m                      ",
    "                         :\033[96m~~\033[0m:                     ",
    "                       .^.\033[96m::\033[0m.^                    ",
    "                      :^  \033[96m..\033[0m :^                   ",
    "                     ^:   \033[96m..\033[0m  .^                  ",
    "                   .^.    \033[96m..\033[0m   .^.                ",
    "                  :^      \033[96m..\033[0m     ~.               ",
    "                 ^:       \033[96m..\033[0m      ^:              ",
    "               .^.        \033[96m..\033[0m       ^:             ",
    "              :^          \033[96m..   h\033[0m    :^            ",
    "             ^:           \033[96m..\033[0m         :^           ",
    "           .^.            \033[96m..\033[0m          .^.         ",
    "          :^              \033[96m..\033[0m           .^.        ",
    "         ^:               \033[96m..\033[0m             ^:       ",
    "       .^.                \033[96m..\033[0m              ^:      ",
    "      :^                  \033[96m:.\033[0m               :^     ",
    "     ^:           ....... \033[96m::\033[0m .....          :^    ",
    "   .^.  ......''''        \033[96m..\033[0m      ''''.....  .~   ",
    "  :^..''                  \033[96m..\033[0m               ''..~: ",
    " ~:                       \033[96m.\033[95m.....................!^\033[0m",
    " ^:                                \033[95mr\033[0m            .^:",
    "  .^::..                                   ..:^:. ",
    "     ''::::::........         .......:::::::''    ",
    "            '''''::::::::::::::::'''''           ",
]

clear = lambda: os.system("cls")


def clean(n) -> None:
    for _ in range(n):
        sys.stdout.write("\033[F")
        sys.stdout.write("\033[K")


def clean2(n) -> None:
    sys.stdout.write("\033[F")
    print(" " * n, end="\r")


def vstup_float(txt) -> float:
    while True:
        a: str = ""
        try:
            return float(a := input(txt))
        except:
            clean2(len(txt) + len(a))
            print("\033[93mChybný vstup\033[0m", end="\r")
            time.sleep(1)


def vstup_float_min(txt, min) -> int:
    while True:
        a: str = ""
        try:
            if int((a := input(txt))) > min:
                return int(a)
            raise ValueError
        except:
            clean2(len(txt) + len(a))
            print("\033[93mChybný vstup\033[0m", end="\r")
            time.sleep(1)


def zadejte_strany(
    *args, počet_stran=0, výška=0, poloměr=0, kolikastranný=0, **kwargs
) -> None:
    for a in args:
        rozměry[a] = vstup_float(f"Zadejte \033[93m{a}: ")
        print("\033[0m", end="")
    if kolikastranný:
        rozměry["kolikastranný"] = vstup_float_min("Zadejte kolikati je stranný: ", 2)
        # počet_stran = rozměry["kolikastranný"]

    if počet_stran:
        rozměry["strany"] = [
            x
            for n in range(počet_stran)
            for x in [vstup_float_min(f"Zadejte stranu \033[93m{chr(n+97)}: ", 0)]
            if not print("\033[0m", end="")
        ]
    if výška:
        rozměry["výška"] = vstup_float("Zadejte \033[96mvýšku: ")
        print("\033[0m", end="")
    if poloměr:
        rozměry["poloměr"] = vstup_float("Zadejte \033[95mpoloměr: ")
        print("\033[0m", end="")


class ED:
    def __init__(self, těleso="") -> None:
        self.těleso: str = těleso
        self.oběm: float = 0
        self.povrch: float = 0
        try:
            for line in globals()[self.těleso.replace(" ", "_")]:
                print(40 * " " + line)
            for _ in range(len(globals()[self.těleso.replace(" ", "_")])):
                sys.stdout.write("\033[F")
        except:
            pass
        print(f"\n\033[95m{self.těleso.capitalize()}\033[0m\n")

    def output(self) -> None:
        print(
            f"\n\033[95mOběm\033[0m   {self.těleso} je: \033[96m{round(self.oběm, 4)}\033[0m"
        )
        print(
            f"\033[95mPovrch\033[0m {self.těleso} je: \033[96m{round(self.povrch, 4)}\033[0m"
        )
        input("\nStiskni enter pro pokračování...")
        # sys.stdout.write("\033[F")
        # print("\033[33m" + "─" * 32 + "\033[0m")
        clear()

    # obecná tělesa

    def krychle(self) -> None:
        zadejte_strany(počet_stran=1)
        self.oběm = rozměry["strany"][0] ** 3
        self.povrch = 6 * rozměry["strany"][0] ** 2
        self.output()

    def kvádr(self) -> None:
        zadejte_strany(počet_stran=3)
        self.oběm = rozměry["strany"][0] * rozměry["strany"][1] * rozměry["strany"][2]
        self.povrch = 2 * (
            rozměry["strany"][0] * rozměry["strany"][1]
            + rozměry["strany"][0] * rozměry["strany"][2]
            + rozměry["strany"][1] * rozměry["strany"][2]
        )
        self.output()

    def hranol(self) -> None:
        zadejte_strany(počet_stran=1, výška=1, kolikastranný=1)
        self.oběm = (
            rozměry["kolikastranný"]
            * rozměry["výška"]
            * rozměry["strany"][0] ** 2
            / (4 * mt.tan(mt.pi / rozměry["kolikastranný"]))
        )
        self.povrch = rozměry["kolikastranný"] * rozměry["strany"][0] * rozměry[
            "výška"
        ] + rozměry["kolikastranný"] * rozměry["strany"][0] ** 2 / (
            2 * mt.tan(mt.pi / rozměry["kolikastranný"])
        )
        self.output()

    def jehlan(self) -> None:
        zadejte_strany(počet_stran=1, výška=1, kolikastranný=1)
        self.oběm = (
            rozměry["kolikastranný"]
            * rozměry["výška"]
            * rozměry["strany"][0] ** 2
            / (12 * mt.tan(mt.pi / rozměry["kolikastranný"]))
        )
        self.povrch = rozměry["kolikastranný"] * rozměry["strany"][0] * (
            rozměry["výška"] ** 2
            + rozměry["strany"][0] ** 2
            / (4 * mt.tan(mt.pi / rozměry["kolikastranný"]) ** 2)
        ) ** 0.5 / 2 + rozměry["kolikastranný"] * rozměry["strany"][0] ** 2 / (
            4 * mt.tan(mt.pi / rozměry["kolikastranný"])
        )
        self.output()

    def kužel(self) -> None:
        zadejte_strany(poloměr=1, výška=1)
        self.oběm = mt.pi * rozměry["poloměr"] ** 2 * rozměry["výška"] / 3
        self.povrch = (
            mt.pi
            * rozměry["poloměr"]
            * (rozměry["poloměr"] ** 2 + rozměry["výška"] ** 2) ** 0.5
        )
        self.output()

    def válec(self) -> None:
        zadejte_strany(výška=1, poloměr=1)
        self.oběm = mt.pi * rozměry["poloměr"] ** 2 * rozměry["výška"]
        self.povrch = 2 * mt.pi * rozměry["poloměr"] * rozměry["výška"]
        self.output()

    def koule(self) -> None:
        zadejte_strany(poloměr=1)
        self.oběm = 4 / 3 * mt.pi * rozměry["poloměr"] ** 3
        self.povrch = 4 * mt.pi * rozměry["poloměr"] ** 2
        self.output()

    def torus(self) -> None:
        zadejte_strany("vnitřní poloměr", poloměr=1)
        self.oběm = (
            2 * mt.pi**2 * rozměry["poloměr"] * rozměry["vnitřní poloměr"] ** 2
        )
        self.povrch = 4 * mt.pi**2 * rozměry["poloměr"] * rozměry["vnitřní poloměr"]
        self.output()

    # komolá tělesa

    def komolý_jehlan(self) -> None:
        zadejte_strany(
            "délku spodní podstavy", "délku horní podstavy", výška=1, kolikastranný=1
        )
        s1 = (rozměry["kolikastranný"] * rozměry["délku spodní podstavy"] ** 2) / (
            4 * mt.tan(mt.pi / rozměry["kolikastranný"])
        )
        s2 = (rozměry["kolikastranný"] * rozměry["délku horní podstavy"] ** 2) / (
            4 * mt.tan(mt.pi / rozměry["kolikastranný"])
        )
        r1 = rozměry["délku spodní podstavy"] / (
            2 * mt.tan(mt.pi / rozměry["kolikastranný"])
        )
        r2 = rozměry["délku horní podstavy"] / (
            2 * mt.tan(mt.pi / rozměry["kolikastranný"])
        )
        c = mt.sqrt((r1 - r2) ** 2 + rozměry["výška"] ** 2)
        spl = (
            (rozměry["délku spodní podstavy"] + rozměry["délku horní podstavy"])
            * c
            * rozměry["kolikastranný"]
            / 2
        )
        self.oběm = (s1 + mt.sqrt(s1 * s2) + s2) * rozměry["výška"] / 3
        self.povrch = s1 + s2 + spl
        self.output()

    def komolý_kužel(self) -> None:
        zadejte_strany("poloměr spodní podstavy", "poloměr vrchní podstavy", výška=1)
        self.oběm = (
            mt.pi
            * rozměry["výška"]
            * (
                rozměry["poloměr spodní podstavy"] ** 2
                + rozměry["poloměr vrchní podstavy"] ** 2
                + rozměry["poloměr spodní podstavy"]
                * rozměry["poloměr vrchní podstavy"]
            )
            / 3
        )
        self.povrch = mt.pi * (
            (rozměry["poloměr spodní podstavy"] + rozměry["poloměr vrchní podstavy"])
            * mt.sqrt(
                rozměry["poloměr spodní podstavy"] ** 2
                - 2
                * rozměry["poloměr spodní podstavy"]
                * rozměry["poloměr vrchní podstavy"]
                + rozměry["poloměr vrchní podstavy"] ** 2
                + rozměry["výška"] ** 2
            )
            + rozměry["poloměr spodní podstavy"] ** 2
            + rozměry["poloměr vrchní podstavy"] ** 2
        )
        self.output()

    # platónská tělesa

    def čtyřstěn(self) -> None:
        zadejte_strany(počet_stran=1)
        self.oběm = mt.sqrt(2) * rozměry["strany"][0] ** 3 / 12
        self.povrch = mt.sqrt(3) * rozměry["strany"][0] ** 2
        self.output()

    def osmistěn(self) -> None:
        zadejte_strany(počet_stran=1)
        self.oběm = mt.sqrt(2) * rozměry["strany"][0] ** 3 / 3
        self.povrch = mt.sqrt(3) * 2 * rozměry["strany"][0] ** 2
        self.output()

    def dvanáctistěn(self) -> None:
        zadejte_strany(počet_stran=1)
        self.oběm = (mt.sqrt(5) * 7 + 15) * rozměry["strany"][0] ** 3 / 4
        self.povrch = mt.sqrt(25 + 10 * mt.sqrt(5)) * 3 * rozměry["strany"][0] ** 2
        self.output()

    def dvacetistěn(self) -> None:
        zadejte_strany(počet_stran=1)
        self.oběm = (mt.sqrt(5) + 3) * 5 * rozměry["strany"][0] ** 3 / 12
        self.povrch = mt.sqrt(3) * 5 * rozměry["strany"][0] ** 2
        self.output()


def pravidelné_mnohostěny() -> None:
    clean(len(tělesa) + 4)
    print(
        "\nVšechna podporovaná pravidelná tělesa:\n",
        *[f"{i}: {n}\n" for i, n in enumerate(mnohostěny)],
    )
    těleso: str = input("Zadej těleso: ")
    try:
        těleso = mnohostěny[int(těleso)]
    except:
        pass
    if těleso == "_zpět_" or těleso not in mnohostěny:
        clean(len(mnohostěny) + 4)
        return
    elif těleso in mnohostěny:
        clean(len(mnohostěny) + 4)
        getattr(globals()["ED"](těleso=těleso), těleso)()
    else:
        exit()


def komolá() -> None:
    clean(len(tělesa) + 4)
    print(
        "\nVšechna podporovaná pravidelná tělesa:\n",
        *[f"{i}: {n}\n" for i, n in enumerate(komolá_tělesa)],
    )
    těleso: str = input("Zadej těleso: ")
    try:
        těleso = komolá_tělesa[int(těleso)]
    except:
        pass
    if těleso == "_zpět_" or těleso not in komolá_tělesa:
        clean(len(komolá_tělesa) + 4)
        return
    elif těleso in komolá_tělesa:
        clean(len(komolá_tělesa) + 4)
        getattr(globals()["ED"](těleso=těleso), těleso.replace(" ", "_"))()
    else:
        exit()


def main() -> None:
    print(
        "\nVšechna podporovaná pravidelná tělesa:\n",
        *[f"{i}: {n}\n" for i, n in enumerate(tělesa)],
    )
    těleso: str = input("Zadej těleso: ")
    try:
        těleso = tělesa[int(těleso)]
    except:
        pass
    if těleso == "*komolá tělesa":
        komolá()
        return
    elif těleso == "*pravidelné mnohostěny":
        pravidelné_mnohostěny()
        return
    elif těleso == "_exit_":
        exit()
    elif těleso in tělesa:
        clean(len(tělesa) + 4)
        getattr(globals()["ED"](těleso=těleso), těleso)()
    else:
        clear()
        exit()


while True:
    rozměry = {
        "strany": [],
        "výška": 0,
        "poloměr": 0,
        "kolikastranný": 0,
    }
    main()
