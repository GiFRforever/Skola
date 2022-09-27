a = None
while a is None:
    try:
        a = int(input("Délka látky: "))
    except:
        print("Vložte číslo!!")
latka = a

a = None
while a is None:
    try:
        a = int(input("Délka kusu: "))
    except:
        print("Vložte číslo!!")
kus = a
if latka//kus == 1:
    print("Látka dostačuje pro:", latka//kus, "kus")
elif latka//kus in range(1,5):
    print("Látka dostačuje pro:", latka//kus, "kusy")
else:
	print("Látka dostačuje pro:", latka//kus, "kusů")

if latka%kus == 1:
    print("Odpad činí: ", latka%kus, "jednotku")
elif latka%kus in range(1,5):
    print("Odpad činí: ", latka%kus, "jednotky")
else:
	print("Odpad činí: ", latka%kus, "jednotek")