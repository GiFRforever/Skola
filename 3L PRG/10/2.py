def main():
    N = int(input("Zadejte počet čísel: "))
    soucet = 0
    lichych = 0
    sudych = 0
    for i in range(N):
        cislo = int(input(f"Zadejte {i}. číslo: "))
        if cislo % 2 == 0:
            sudych = sudych + 1
        else:
            lichych = lichych + 1
        soucet = soucet + cislo
    print("Sudých je", sudych)
    print("Lichých je", lichych)
    print("Průměr je", soucet / N)


main()
