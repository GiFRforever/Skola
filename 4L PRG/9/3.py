def vstup_znak(txt: str) -> str:
    while True:
        znak = input(txt)
        if not znak.isalpha() or len(znak) != 1:
            print("Zadejte pouze jedno písmeno!")
        else:
            return znak


znak = vstup_znak("Zadejte písmeno: ")
with open("pyramida.txt", "w") as pyramida:
    for i in range(1, 101):
        pyramida.write(znak * i + "\n")
