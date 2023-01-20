def main():
    N = int(input("Zadejte počet čísel: "))
    nejvetsi = 0
    for i in range(N):
        cislo = int(input(f"Zadejte {i}. číslo: "))
        if cislo > nejvetsi:
            nejvetsi = cislo
    print("Největší číslo je", nejvetsi)


main()
