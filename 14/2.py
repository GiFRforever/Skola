import random

print("Myslím si náhodné číslo do 100.")
num: int = random.randint(1, 100)
guess: int = int(input("Zkus ho uhodnout: "))
tries: int = 1
if guess == num:
    print("Trefa!")
else:
    while guess != num:
        if guess > num:
            print("Moc vysoko!")
            guess = int(input("Zkus ho uhodnout: "))
            tries += 1
        elif guess < num:
            print("Moc nízko!")
            guess = int(input("Zkus ho uhodnout: "))
            tries += 1
    print("Trefa!")
if tries == 1:
    st = ""
    po = "!"
elif tries > 1 and tries < 5:
    st = "y"
    po = "y!"
else:
    st = "o"
    po = "ů!"

print(f"Stačil{st} ti {tries} pokus{po}")
