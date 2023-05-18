from time import perf_counter
def pluck(list_dict: list[dict], key: str):
    return [d.get(key) for d in list_dict]

# test print
t1 = perf_counter()
for _ in range(100000):
    pluck([{'a': 1}, {'a': 2}], 'a') # [1, 2]
    pluck([{'a': 1, 'b': 3}, {'a': 2}], 'b') # [3, None]
    pluck([{'a': 1, 'b': 3}, {'a': 2}], 'c') # [None, None]
    pluck([{'a': 1, 'b': 3}, {'a': 2, 'b': 4}], 'b') # [3, 4]
    pluck([{'a': 1, 'b': 3}, {'a': 2, 'b': 4}], 'a') # [1, 2]
t: float = perf_counter() - t1
print(f"pluck: {t:.6f} seconds")

print(list(map(lambda list_dict, key: [d.get(key) for d in list_dict], [[{'a': 1}, {'a': 2}], [{'a': 1, 'b': 3}, {'a': 2}], [{'a': 1, 'b': 3}, {'a': 2}], [{'a': 1, 'b': 3}, {'a': 2, 'b': 4}], [{'a': 1, 'b': 3}, {'a': 2, 'b': 4}]], ['a', 'b', 'c', 'b', 'a'])))