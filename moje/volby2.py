import random as rnd

kolik_kandidátů = 10
kolik_voličů = 3
kolik_postupujicích = 2
iterací = 1000

pole: list[list[int]] = []
default = [x for x in range(kolik_kandidátů)]

for i in range(kolik_voličů):
    rnd.shuffle(default)
    pole.append(default.copy())
print(pole)

pocitadlo = [[0 for _ in range(kolik_kandidátů)] for _ in range(kolik_kandidátů)]
for l in pole:
    for i, v in enumerate(l):
        pocitadlo[v][i] += 1

print(pocitadlo)
