"""
s = None
while s is None:
    try:
        s = int(input("Zadej hodnotu: "))
    except:
        print("Vložte číslo!!")
a = None
while a is None:
    try:
        a = int(input("Zadej hodnotu: "))
    except:
        print("Vložte číslo!!")
print(a+s)
"""


def zadanicisla(a):
    while a is None:
        try:
            a = int(input("Zadej hodnotu: "))
        except:
            print("Vložte číslo!!")
