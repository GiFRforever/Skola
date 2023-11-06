with open("text.txt", "r") as text, open("jinytext.txt", "w") as jiny:
    for řádek in reversed(text.readlines()):
        for znak in reversed(řádek):
            jiny.write(znak)
