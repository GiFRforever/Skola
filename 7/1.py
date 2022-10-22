import random
cisla = []
for i in range(5):
    cisla.append(random.randint(1,6))
print(f"Kostka hodila {cisla}, průměr hodů je {sum(cisla)/len(cisla)}")