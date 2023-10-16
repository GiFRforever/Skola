from random import randint
with open("cisla.txt", "w") as cisla:
    for _ in range(10):
        cisla.write(f"{(c := randint(1, 100)):>3}^2 = {c*c}\n")