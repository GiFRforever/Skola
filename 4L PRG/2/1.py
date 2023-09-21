from random import randint as ri

print(
    (seznam := list(tuple(ri(1, 100) for _ in range(3)) for _ in range(10))),
    *seznam,
    sep="\n",
)
