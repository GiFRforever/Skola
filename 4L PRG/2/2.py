import sys, platform, os

reqmetatfrst = True

# requirements vvv

requirements = ["pyperclip", "msvcrt"]

for module in requirements:
    try:
        exec(f"import {module}")

    except ModuleNotFoundError:
        import pip
        import subprocess
        import sys

        def install(package):
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])

        install(module)
        exec(f"import {module}")
        
        reqmetatfrst = False


from ctypes import wintypes



    



# keypuller vvv

global isWindows

if (p := platform.uname()[0]) == "Windows":
    try:
        from win32api import STD_INPUT_HANDLE
        from win32console import GetStdHandle, KEY_EVENT, ENABLE_ECHO_INPUT, ENABLE_LINE_INPUT, ENABLE_PROCESSED_INPUT
        isWindows = True
    except ModuleNotFoundError:
        import pip
        import subprocess
        import sys

        def install(package):
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])

        install("pywin32")
        from win32api import STD_INPUT_HANDLE
        from win32console import GetStdHandle, KEY_EVENT, ENABLE_ECHO_INPUT, ENABLE_LINE_INPUT, ENABLE_PROCESSED_INPUT
        isWindows = True

        reqmetatfrst = False
    
    # GetStdHandle = ctypes.windll.kernel32.GetStdHandle
    # STD_INPUT_HANDLE = -10
    # ENABLE_LINE_INPUT = 2
    # ENABLE_ECHO_INPUT = 4
    # ENABLE_PROCESSED_INPUT = 1
    # ENABLE_MOUSE_INPUT = 16
    # ENABLE_WINDOW_INPUT = 8
    # KEY_EVENT = 1

elif p == "Linux":
    import sys
    import select
    import termios
    isWindows = False

class KeyPuller():
    def __enter__(self):
        global isWindows
        if isWindows:
            self.capturedChars = []
        else:
            # Save the terminal settings
            self.fd = sys.stdin.fileno()
            self.new_term = termios.tcgetattr(self.fd)
            self.old_term = termios.tcgetattr(self.fd)

            # New terminal setting unbuffered
            self.new_term[3] = (self.new_term[3] & ~termios.ICANON & ~termios.ECHO)
            termios.tcsetattr(self.fd, termios.TCSAFLUSH, self.new_term)

        return self

    def __exit__(self, type, value, traceback):
        if not isWindows:
            termios.tcsetattr(self.fd, termios.TCSAFLUSH, self.old_term)

    def poll(self) -> str|None:
        if isWindows:
            if not len(self.capturedChars) == 0:
                return self.capturedChars.pop(0)

            while msvcrt.kbhit():
                char = msvcrt.getch()
                self.capturedChars.append(char.decode("utf-8"))

            if not len(self.capturedChars) == 0:
                return self.capturedChars.pop(0)
            else:
                return None
        else:
            dr, dw, de = select.select([sys.stdin], [], [], 0)
            if not dr == []:
                return os.read(self.fd, 1).decode("utf-8")
            return None

# úkol vvv

white: dict[str, str] = {"Novák": "+420 603 763 466", "Bittner": "+420 792 333 630", "Česnek": "+420 776 324 232", "Glac": "+420 735 968 231"}

lines: list[str] = []

def TelCheck(tel: str) -> str:
    tel = tel.replace(" ", "")
    if tel[0] == "+":
        tel = "+" + ' '.join(tel[i:i+3] for i in range(1, len(tel), 3))
    else:
        tel = "+420 "+' '.join(tel[i:i+3] for i in range(0, len(tel), 3))
    return tel

def DoLines():
    global lines
    lines = [f"{(name+':'):{max([len(name) for name in white])+1}} {white[name]}" for name in white]
    lines.sort()
# print(*lines, sep="\n")


if p == "Windows":
    clear = lambda: os.system("cls")

    def GoToTop(n) -> None:
        for _ in range(n):
            sys.stdout.write("\033[F")
    
    def clean(n) -> None:
        for _ in range(n):
            sys.stdout.write("\033[F")
            sys.stdout.write("\033[K")

elif p == "Linux":
    clear = lambda: os.system("clear")

    def GoToTop(n) -> None:
        for _ in range(n):
            sys.stdout.write("\x1b[1A")

    def clean(n) -> None:
        for _ in range(n):
            sys.stdout.write("\x1b[1A")
            sys.stdout.write("\x1b[2K")

else:
    exit("Unsupported os")

# tady se to ukazuje
def display() -> None:
    global lines
    global lineon


    for i in range(lineon):
        print(lines[i])
    
    print(f"\33[100m{lines[lineon]}\33[0m")

    for i in range(lineon+1, len(lines)):
        print(lines[i])
    
    print("\33[8m", end="")


lineon: int = 0

def vstup() -> str|None:
    print("\33[8m", end="")
    with KeyPuller() as keyPuller:
        while True:
            if (c:= keyPuller.poll()):
                print("\33[0m", end="")
                return c

def main() -> None:
    global lines
    global lineon
    clear()

    # meníčko
    print("""
8 - nadohu
2 - dolů
0 - kopírovat
i - vložení
d - mazání
s - hledání
""")

    # tady si uživatel vybírá akci
    DoLines()
    display()
    while True:
        # c = keyPuller.poll()
        c = vstup()
        match c:
            case "8":
                if lineon:
                    lineon -= 1
                GoToTop(len(lines))
                
            case "2":
                if lineon < len(lines)-1:
                    lineon += 1
                GoToTop(len(lines))
                
            case "i":
                # vložení
                nj: str = input("Zadejte jméno: ")
                nč: str = input("Zadejte telefonní číslo: ")
                nč = TelCheck(nč)
                white[nj] = nč
                clean(2+len(lines))
                DoLines()
            case "d":
                # mazání
                name = lines[lineon].split(":")[0]
                if input(f"Přejete si smazat kontakt '{name}'? [Y/n]") in ["Y","y", ""]:
                    white.pop(name)
                    clean(1+len(lines))
                    DoLines()
                else:
                    clean(1)
                    GoToTop(len(lines))
            case "s":
                # hledání
                clean(len(lines))
                with KeyPuller() as keyPuller:
                    hl = ""
                    srch = [""]
                    print("""
7 - reset hledání
1 - konec hledání
0 - zkopírovat číslo

""")
                    while True:
                        if (c := keyPuller.poll()):
                            clean(len(srch))
                            if c == "7":
                                hl = ""
                            elif c == "1":
                                break
                            elif c == "0":
                                pyperclip.copy(srch[0].split(":")[0])
                            srch = [line for line in lines if hl in line.lower()]
                            hl += c.lower()
                            print(*srch, sep="\n")
                            
            case "0":
                pyperclip.copy(lines[lineon].split(":")[0])
            case "e":
                break
            case _:
                continue
        display()

if __name__ == "__main__":
    if reqmetatfrst:    
        main()
    else:
        for i in range(5,-1,-1):
            print(f"Tak znovu za {i}", end="\r")
        os.startfile("2.py")