from random import randint

r: int = randint(100, 100_000)
print(f"Vygeneroval jsem {r}")
print(f"Jeho ciferný součet je {sum(int(c) for c in str(r))}")
