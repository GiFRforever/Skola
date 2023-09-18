lowcharset: dict[str, int] = {chr(i): 0 for i in range(97, 123)}
uprcharset: dict[str, int] = {chr(i): 0 for i in range(65, 91)}
noncharset: dict[str, int] = {}
specialcharset: dict[str, int] = {
    chr(i): 0
    for i in [
        *range(192, 215),
        *range(216, 247),
        *range(248, 592),
        # *range(),
        # *range(),
        # *range(),
    ]
}
# řetězec: str = input("Zadejte řetězec: ")
# Báseň o bagru
# řetězec: str = "Báseň o bagru, který byl zlověstný, jehož věci byly všechny špatné, neboť byl vůči svým spolužákům velmi zlobivý a byl také velmi náladový. Všichni ho měli rádi, protože byl velmi vtipný a všichni se mu smáli. Lidé ho měli rádi, protože byl velmi vtipný a všichni se mu smáli."
# zadání
řetězec: str = "Python je skvely objektove orientovany, interpretovany a interaktivni programovaci jazyk."
for znak in řetězec:
    if znak in lowcharset:
        lowcharset[znak] += 1
    elif znak in uprcharset:
        uprcharset[znak] += 1
    elif znak in specialcharset:
        specialcharset[znak] += 1
    elif znak in noncharset:
        noncharset[znak] += 1
    else:
        noncharset[znak] = 1

# kolik obsahuje řetězec znaků
print(f"Řetězec obsahuje {len(řetězec)} znaků.")
# kolik obsahuje řetězec písmen
print(f"Řetězec obsahuje {sum(lowcharset.values()) + sum(uprcharset.values())} písmen.")
# kolik obsahuje písmen "a", "e"
print(
    f"Řetězec obsahuje {lowcharset['a'] + uprcharset['A']} písmen 'a' a {lowcharset['e'] + uprcharset['E']} písmen 'e'."
)
# vytiskne slovo "python" tolikrát, kolikrát je tam písmeno "o"
print("python" * lowcharset["o"])
# Je v řetězci písmeno "x"?
if lowcharset["x"] + uprcharset["X"] > 0:
    print("Řetězec obsahuje písmeno 'x'.")
else:
    print("Řetězec neobsahuje písmeno 'x'.")
# 50 krát 12. znak řetězce
print(řetězec[11] * 50)
# zaměň "e" za "x"
print(řetězec.replace("e", "x"))
# velkými písmeny
print(řetězec.upper())
