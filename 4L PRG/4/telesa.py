import time


class Telesa:
    def __init__(self) -> None:
        self.PI: float = 3.14159
        self.rozměry: dict = {
            "strany": [],
            "výška": 0,
            "poloměr": 0,
            "kolikastranný": 0,
        }

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
