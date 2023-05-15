def vstup(txt) -> str:
    while True:
        sequence: str = input(txt)
        for s in sequence:
            if s not in "wsad":
                print("Neplatný postup")
                continue
        else:
            return sequence


def time_check(sequence: str) -> bool:
    sequence = sequence.lower()
    w: int = sequence.count("w")
    s: int = sequence.count("s")
    a: int = sequence.count("a")
    d: int = sequence.count("d")
    if w == s and a == d and w + s + a + d == 12:
        return True
    else:
        return False


sequence: str = vstup("Zadej postup: ")
if time_check(sequence):
    print("Postup je správný")
else:
    print("Postup je špatný")
