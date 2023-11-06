def vstup_znak(txt: str, excluded: list[str]) -> str:
    while True:
        znak = input(txt)
        if znak in excluded or len(znak) != 1:
            print("Zadejte pouze jeden znak!")
        else:
            return znak


stary = vstup_znak("Zadejte znak, který chcete nahradit: ", [])
novy = vstup_znak("Zadejte znak, kterým jej chcete nahradit: ", [stary])
with open("text.txt", "r") as text, open("jinytext.txt", "w") as jiny:
    for řádek in text.readlines():
        for znak in řádek:
            if znak == stary:
                jiny.write(novy)
            else:
                jiny.write(znak)
