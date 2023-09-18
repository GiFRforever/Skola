from random import randint
input("Zadejte uživatelské jméno: ")
input("Zadejte heslo: ")
if randint(0,5):
    print("Přihlášení nebylo úspěšné.")
else:
    print("Přihlášení bylo úspěšné.")