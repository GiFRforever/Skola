import time, os, sys


class Telesa:
    def __init__(self, těleso="") -> None:
        self.obrazky = {
            "koule": [
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
            ],
            "kvádr": [
                "                                        ",
                "    .:...............................:^ ",
                "  .:.:                              :.^ ",
                " ^:..^............................\033[93m:\033[0m:  : ",
                ".:  .:                            \033[93m:\033[0m   : ",
                " :   :                            \033[93m:\033[0m   : ",
                " :   :                            \033[93m: c\033[0m : ",
                " :   :                            \033[93m:\033[0m   : ",
                " :   :                            \033[93m:\033[0m   :.",
                " :  ::............................\033[93m^\033[0m..\033[93m:^\033[0m ",
                " ^.:                              \033[93m:.:.  b\033[0m",
                " \033[93m^:...............................:.\033[0m    ",
                "                 \033[93ma\033[0m                       ",
            ],
            "krychle": [
                "                             ",
                "    .:..................:^ ",
                "  .:.:                 :.^ ",
                " ^:..^...............\033[93m:\033[0m:  : ",
                ".:  .:               \033[93m:\033[0m   : ",
                " :   :               \033[93m:\033[0m   : ",
                " :   :               \033[93m: a\033[0m : ",
                " :   :               \033[93m:\033[0m   : ",
                " :   :               \033[93m:\033[0m   :",
                " :  ::...............\033[93m:\033[0m...\033[93m:\033[0m ",
                " ^.:                 \033[93m: .'  \033[93ma\033[0m",
                " \033[93m^:..................:'\033[0m    ",
                "            \033[93ma\033[0m               ",
            ],
        }

        self.PI: float = 3.14159
        self.těleso: str = těleso
        # vrací velikost konzole
        self.velikost = lambda: os.get_terminal_size()
        self.rozměry: dict = {
            "strany": [],
            "výška": 0,
            "poloměr": 0,
            "kolikastranný": 0,
        }

        try:
            # print(self.obrazky[self.těleso.replace(" ", "_")][0])
            if (
                len(self.obrazky[self.těleso.replace(" ", "_")][0]) + 40
                > self.velikost()[0]
                or len(self.obrazky[self.těleso.replace(" ", "_")]) > self.velikost()[1]
            ):
                raise Exception
            for line in self.obrazky[self.těleso.replace(" ", "_")]:
                print(40 * " " + line)
            for _ in range(len(self.obrazky[self.těleso.replace(" ", "_")])):
                sys.stdout.write("\033[F")
        except:
            pass
        print(f"\n\033[95m{self.těleso.capitalize()}\033[0m\n")

    # vstupy
    def vstup_float(self, txt) -> float:
        while True:
            a: str = ""
            try:
                return float(a := input(txt))
            except:
                clean2(len(txt) + len(a))
                print("\033[93mChybný vstup\033[0m", end="\r")
                time.sleep(1)

    def vstup_float_min(self, txt, min) -> int:
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

    # zadávání rozměrů těles
    def zadejte_strany(
        self, *args, počet_stran=0, výška=0, poloměr=0, kolikastranný=0, **kwargs
    ) -> None:
        for a in args:
            if type(a) == tuple:
                self.rozměry[a[0]] = self.vstup_float(
                    f"Zadejte \033[{str(a[1])}m{a[0]}: "
                )
                print("\033[0m", end="")
            else:
                self.rozměry[a] = self.vstup_float(f"Zadejte \033[93m{a}: ")
                print("\033[0m", end="")
        if kolikastranný:
            self.rozměry["kolikastranný"] = self.vstup_float_min(
                "Zadejte kolikati je stranný: ", 2
            )

        if počet_stran:
            self.rozměry["strany"] = [
                x
                for n in range(počet_stran)
                for x in [
                    self.vstup_float_min(f"Zadejte stranu \033[93m{chr(n+97)}: ", 0)
                ]
                if not print("\033[0m", end="")
            ]
        if poloměr:
            self.rozměry["poloměr"] = self.vstup_float("Zadejte \033[95mpoloměr: ")
            print("\033[0m", end="")
        if výška:
            self.rozměry["výška"] = self.vstup_float("Zadejte \033[96mvýšku: ")
            print("\033[0m", end="")

    def krychle(self) -> None:
        self.zadejte_strany(počet_stran=1)
        self.objem = self.rozměry["strany"][0] ** 3
        self.povrch = 6 * self.rozměry["strany"][0] ** 2
        return (self.objem, self.povrch)

    def kvádr(self) -> None:
        self.zadejte_strany(počet_stran=3)
        self.objem = (
            self.rozměry["strany"][0]
            * self.rozměry["strany"][1]
            * self.rozměry["strany"][2]
        )
        self.povrch = 2 * (
            self.rozměry["strany"][0] * self.rozměry["strany"][1]
            + self.rozměry["strany"][0] * self.rozměry["strany"][2]
            + self.rozměry["strany"][1] * self.rozměry["strany"][2]
        )
        return (self.objem, self.povrch)

    def koule(self) -> None:
        self.zadejte_strany(poloměr=1)
        self.objem = 4 / 3 * self.PI * self.rozměry["poloměr"] ** 3
        self.povrch = 4 * self.PI * self.rozměry["poloměr"] ** 2
        return (self.objem, self.povrch)
