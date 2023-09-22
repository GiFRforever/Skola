import sys
import select
import os
import json

try:
    import msvcrt
except ImportError:
    isWindows = False
    import termios
else:
    isWindows = True

try:
    import pyperclip

except ModuleNotFoundError:
    import pip
    import subprocess

    def install(package):
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

    install("pyperclip")
    import pyperclip


if isWindows:

    class KeyPuller:
        def __enter__(self):
            self.capturedChars: list[str] = []

            return self

        def __exit__(self, type, value, traceback) -> None:
            pass

        def pull(self) -> str | None:
            if not len(self.capturedChars) == 0:
                return self.capturedChars.pop(0)

            while msvcrt.kbhit():
                char: bytes = msvcrt.getch()
                self.capturedChars.append(char.decode("utf-8"))

            if not len(self.capturedChars) == 0:
                return self.capturedChars.pop(0)
            else:
                return None

else:

    class KeyPuller:
        def __enter__(self):
            # Save the terminal settings
            self.fd: int = sys.stdin.fileno()
            self.new_term = termios.tcgetattr(self.fd)
            self.old_term = termios.tcgetattr(self.fd)

            # New terminal setting unbuffered
            self.new_term[3] = self.new_term[3] & ~termios.ICANON & ~termios.ECHO
            termios.tcsetattr(self.fd, termios.TCSAFLUSH, self.new_term)

            return self

        def __exit__(self, type, value, traceback) -> None:
            termios.tcsetattr(self.fd, termios.TCSAFLUSH, self.old_term)

        def pull(self) -> str | None:
            dr, dw, de = select.select([sys.stdin], [], [], 0)
            if not dr == []:
                return os.read(self.fd, 1).decode("utf-8")
            return None


def vstup(keypuller) -> str:
    while True:
        if c := keypuller.pull():
            return c  # c je klávesa, kterou uživatel zmáčkl


# úkol vvv


lines: list[str] = []
white: dict[str, str] = {}


def lodewhite() -> None:
    global white
    global lines
    try:
        with open("white.json", "r") as f:
            white = json.load(f)
    except FileNotFoundError:
        white = {
            "Novák": "+420 603 763 466",
            "Bittner": "+420 792 333 630",
            "Česnek": "+420 776 324 232",
            "Glac": "+420 735 968 231",
        }


def savewhite() -> None:
    global white
    with open("white.json", "w") as f:
        json.dump(white, f)


def TelCheck(tel: str) -> str:
    tel = tel.replace(" ", "")
    if tel[0] == "+":
        tel = "+" + " ".join(tel[i : i + 3] for i in range(1, len(tel), 3))
    else:
        tel = "+420 " + " ".join(tel[i : i + 3] for i in range(0, len(tel), 3))
    return tel


def DoLines():
    global lines
    lines = [
        f"{(name+':'):{max([len(name) for name in white])+1}} {white[name]}"
        for name in white
    ]
    lines.sort()


if isWindows:
    clear = lambda: os.system("cls")

    def GoToTop(n) -> None:
        for _ in range(n):
            sys.stdout.write("\033[F")

    def clean(n) -> None:
        for _ in range(n):
            sys.stdout.write("\033[F")
            sys.stdout.write("\033[K")

else:
    clear = lambda: os.system("clear")

    def GoToTop(n) -> None:
        for _ in range(n):
            sys.stdout.write("\x1b[1A")

    def clean(n) -> None:
        for _ in range(n):
            sys.stdout.write("\x1b[1A")
            sys.stdout.write("\x1b[2K")


# tady se to ukazuje
def display() -> None:
    global lines
    global lineon

    if len(lines):
        if lineon >= len(lines):
            lineon = len(lines) - 1

        for i in range(lineon):
            print(lines[i])

        print(f"\33[100m{lines[lineon]}\33[0m")

        for i in range(lineon + 1, len(lines)):
            print(lines[i])


lineon: int = 0


def vypis(keypuller):
    global lines
    global lineon
    clear()

    # meníčko
    print(
        """
8 - nadohu
2 - dolů
0 - kopírovat
i - vložení
d - mazání
s - hledání
e - konec
"""
    )

    # tady si uživatel vybírá akci
    DoLines()
    display()

    while True:
        c: str = vstup(keypuller)
        match c:
            case "8":
                if lineon:
                    lineon -= 1
                GoToTop(len(lines))

            case "2":
                if lineon < len(lines) - 1:
                    lineon += 1
                GoToTop(len(lines))

            case "0":
                pyperclip.copy(white[lines[lineon].split(":")[0]])
                GoToTop(len(lines))

            case "i":
                # vložení
                return "i"

            case "d":
                # mazání
                name = lines[lineon].split(":")[0]
                if input(f"Přejete si smazat kontakt '{name}'? [Y/n]") in [
                    "Y",
                    "y",
                    "",
                ]:
                    white.pop(name)
                    clean(1 + len(lines))
                    DoLines()
                    if not len(lines):
                        clean(2)
                else:
                    clean(1)
                    GoToTop(len(lines))

            case "s":
                # hledání
                clean(len(lines))
                hl = ""
                c = ""
                srch = [""]
                print(
                    """
7 - reset hledání
1 - konec hledání
0 - zkopírovat číslo

"""
                )
                while True:
                    c = vstup(keypuller)
                    clean(len(srch))
                    if c == "7":
                        hl = ""
                    elif c == "1":
                        break
                    elif c == "0":
                        pyperclip.copy(white[srch[0].split(":")[0]])
                    else:
                        hl += c.lower()
                    srch = [line for line in lines if hl in line.lower()]
                    print(*srch, sep="\n")
            case "e":
                # konec
                return "e"

            case _:
                continue
        display()


def main() -> None:
    while True:
        with KeyPuller() as keypuller:
            i: str = vypis(keypuller)

        if i == "i":
            nj: str = input("Zadejte jméno: ")
            nč: str = input("Zadejte telefonní číslo: ")
            nč = TelCheck(nč)
            white[nj] = nč
            savewhite()
        elif i == "e":
            break


if __name__ == "__main__":
    try:
        lodewhite()
        main()
        savewhite()
        clear()
    except KeyboardInterrupt:
        savewhite()
        clear()
    except Exception as e:
        savewhite()
        clear()
        print(e)
    exit("Úpravy ztraceny (-:")
