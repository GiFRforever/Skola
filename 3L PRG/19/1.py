from random import randint

seznam: list[int] = [randint(1, 100) for _ in range(20)]
print(*seznam)
print(
    f"{(m := max(seznam))} je největší prvek v seznamu na pozici {', '.join(str(i+1) for i, x in enumerate(seznam) if x == m)}"
)
