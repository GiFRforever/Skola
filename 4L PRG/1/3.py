zaklad = int(input("Zadejte základ: "))
konec = int(input("Zadejte konec: "))

for i in range(0, konec + 1):
    print(f"{zaklad} x {i} = {zaklad * i}")