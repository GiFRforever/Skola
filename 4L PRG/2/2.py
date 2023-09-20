import sys, platform, os, time
from keypuller import KeyPuller

white: dict[str, str] = {"Novák": "+420 603 763 466", "Bittner": "+420 792 333 630", "Česnek": "+420 776 324 232", "Glac": "+420 735 968 231"}

lines: list[str] = []

def DoLines():
    global lines
    lines = [f"{(name+':'):10} {white[name]}" for name in white]
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

lineon: int = 0
# with KeyPuller() as keyPuller:
# try:
#     keyPuller = KeyPuller()

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
            case "2":
                if lineon < len(lines)-1:
                    lineon += 1
            case "i":
                # vložení
                nj: str = input("Zadejte jméno: ")
                nč: str = input("Zadejte telefonní číslo: ")
                white[nj] = nč
                clean(2)
                DoLines()
            case "d":
                # mazání
                pass
            case "s":
                # hledání
                pass
            case "e":
                break
            case _:
                continue
        GoToTop(len(lines))
        display()
# except:
#     keyPuller.__exit__

if __name__ == "__main__":
    main()