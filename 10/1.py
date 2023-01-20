def main():
    N = int(input("Zadejte počet čísel: "))
    soucet = 0
    for i in range(N):
        cislo = int(input(f"Zadejte {i}. číslo: "))
        soucet = soucet + cislo
    print("Součet čísel je", soucet)


main()
