from random import randint


with open("temp.txt", "w") as f:
    for _ in range(10_000_000):
        f.write(str(randint(15,27)+randint(0,99)/100)+"\n")
    else:
        print("Done")