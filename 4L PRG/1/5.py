find = int(input("Zadejte číslo: "))

last = 0
dist = 2**30
dob: tuple = (0,1)
while True:
    dob = (dob[1], dob[0] + dob[1])
    if dist < (dist := abs(dob[1] - find)):
        print(last)
        break
    last = dob[1]

