a = None
while a is None:
    try:
        a = int(input("Délka strany a: "))
    except:
        print("Vložte číslo!!")
b = None
while b is None:
    try:
        b = int(input("Délky strany b: "))
    except:
        print("Vložte číslo!!")
o = 2 * (a + b)
s = a * b
print("Obvod: ", o)
print("Obsah: ", s)
