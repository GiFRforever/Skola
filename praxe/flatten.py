def flatten(*lst) -> list:
    return sum(([x] if not isinstance(x, list) else flatten(*x)
                for x in lst), [])

print(flatten([1, 2, [3, 4, [5, 6]], 7, 8, [9, 10]]))