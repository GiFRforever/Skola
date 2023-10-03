import os, sys, platform
from difflib import SequenceMatcher
from telesa import Telesa as T

tělesa: list[str] = [
    "_exit_",
    "krychle",
    "kvádr",
    "koule",
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
]

krychle: list[str] = [
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
]


def similar(a, b) -> float:
    return SequenceMatcher(None, a, b).ratio()


# čištění konzole
if (p := platform.uname()[0]) == "Windows":
    clear = lambda: os.system("cls")

    def clean(n) -> None:
        for _ in range(n):
            sys.stdout.write("\033[F")
            sys.stdout.write("\033[K")

    def clean2(n) -> None:
        sys.stdout.write("\033[F")
        print(" " * n, end="\r")

elif p == "Linux":
    clear = lambda: os.system("clear")

    def clean(n) -> None:
        for _ in range(n):
            sys.stdout.write("\x1b[1A")
            sys.stdout.write("\x1b[2K")

    def clean2(n) -> None:
        sys.stdout.write("\x1b[1A")
        print(" " * n, end="\r")

else:
    exit("Unsupported os")

druhý_pád: dict[str, str] = {
    "krychle": "krychle",
    "kvádr": "kvádru",
    "koule": "koule",
}


def output(těleso, objem, povrch) -> None:
    print(
        f"\n\033[95mObjem\033[0m   {druhý_pád[těleso]} je: \033[96m{round(objem, 4)}\033[0m"
    )
    print(
        f"\033[95mPovrch\033[0m {druhý_pád[těleso]} je: \033[96m{round(povrch, 4)}\033[0m"
    )
    input("\nStiskni enter pro pokračování...")
    clear()


def menu() -> None:
    print(
        "\nVšechna podporovaná pravidelná tělesa:\n",
        *[f"{i:>2}: {n}\n" for i, n in enumerate(tělesa)],
    )
    těleso: str = input("Zadejte těleso: ")
    try:
        těleso = tělesa[int(těleso)]
    except:
        podobnost: list[float] = [similar(těleso, n) for n in tělesa]
        i_of_max: int = podobnost.index((maxpod := max(podobnost)))
        if maxpod > 0.6:
            těleso = tělesa[i_of_max]
    if těleso == "_exit_":
        clear()
        exit()
    elif těleso in tělesa:
        clear()
        objem, povrch = getattr(globals()["T"](), těleso)()
        output(těleso, objem, povrch)


if __name__ == "__main__":
    while True:
        menu()
