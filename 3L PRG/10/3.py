def main():
    N = int(input("Zadejte počet tříd: "))
    soucet = 0
    for i in range(N):
        trida = int(input(f"Zadejte počet žáků v {i}. třídě: "))
        soucet = soucet + trida
    print("Průměrný počet žáků ve třídě je", soucet / N)


main()
