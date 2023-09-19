import random as rd

pismena = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#klic = input("Zadejte klíč: ")
#zprava = input("Zadejte zpravu: ")
klic = "xochipilli"
zprava = "nachazi u mechove cesticky"
zprava = zprava.replace(" ", "")

if len(zprava) < len(klic):
    print("Příliž krátká zpráva")
    exit()

#chaos = int(input("Zadejte chaos: "))
chaos = 3

if chaos < 3 or chaos > len(pismena):
    print("3 < chaos < delka abecedy")
    exit()

pismena = list(set(pismena) - set(klic.upper()))

out = "".join(rd.choices(pismena, k=(chaos + rd.randint(-2,3))))

for i, pismenko in enumerate(zprava):
    out = out + klic[i%len(klic)] + str(pismenko) + "".join(rd.choices(pismena, k=(chaos + rd.randint(-2,3))))

print(out)