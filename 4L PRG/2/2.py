import sys, platform, os
import pyperclip as pp
from keypuller import KeyPuller

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


if (p := platform.uname()[0]) == "Windows":
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
                                pp.copy(srch[0].split(":")[0])
                            srch = [line for line in lines if hl in line.lower()]
                            hl += c.lower()
                            print(*srch, sep="\n")
                            
            case "0":
                pp.copy(lines[lineon].split(":")[0])
            case "e":
                break
            case _:
                continue
        display()

if __name__ == "__main__":
    main()