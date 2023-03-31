from datetime import datetime

měsíce: dict[int, str] = {
    1: "ledna",
    2: "února",
    3: "března",
    4: "dubna",
    5: "května",
    6: "června",
    7: "července",
    8: "srpna",
    9: "září",
    10: "října",
    11: "listopadu",
    12: "prosince",
}
while True:
    vstup: str = input("Zadejte datum: ")
    for s in ",-/_:; ":
        vstup = vstup.replace(s, ".")
        vstup = vstup.replace("..", ".")
    try:
        datum: datetime = datetime.strptime(vstup, "%d.%m.%Y")
        break
    except ValueError:
        print("Špatný formát data.")

výstup: str = datum.strftime("%d. %m. %Y")
for číslo, název in měsíce.items():
    výstup = výstup.replace(f" {číslo}. ", f" {název} ")
print(f"Zadali jste datum: {výstup}")
