from random import randint
import unicodedata
def strip_accents(s):
   return ''.join(c for c in unicodedata.normalize('NFD', s)
                  if unicodedata.category(c) != 'Mn')

veci = {
    "kamen": 1,
    "nuzky": 2,
    "papir": 3
}
diakritika = {
    "kámen": 1,
    "nůžky": 2,
    "papír": 3
}
def vstup(txt):
    while True:
        vstup = strip_accents(input(txt))
        if vstup == "q":
            exit()
        if vstup in veci:
            return veci[vstup]
        try:
            if int(vstup) in veci.values():
                return int(vstup)
        except:
            pass
        print("Neplatný vstup")

def vyhraje(a, b):
    if a == b:
        return "\033[93mRemíza\033[0m"
    elif (a == 1 and b == 2) or (a == 2 and b == 3) or (a == 3 and b == 1):
        return "\033[92mVyhráli jste!\033[0m"
    else:
        return "\033[91mProhráli jste\033[0m"

print("Hraje se kámen[1], nůžky[2], papír[3], q pro konec")
while True:
    hrac1 = vstup("Vy: ")
    hrac2 = randint(1, 3)
    print(f"Vy: {list(diakritika.keys())[hrac1-1]}")
    print(f"Počítač: {list(veci.keys())[hrac2-1]}")
    print(vyhraje(hrac1, hrac2))