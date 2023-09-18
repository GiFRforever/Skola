znamky: dict[int, str] = {
    60: "Nedostatečný",
    70: "Dostatečný",
    80: "Dobrý",
    90: "Chvalitebný",
    1000: "Výborný",
}

skore: float  = float(input("Zadejte skóre: "))

for znamka in znamky:
    if skore < znamka:
        print(znamky[znamka])
        break