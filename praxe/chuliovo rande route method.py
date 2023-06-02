def vstup(txt) -> str:
    while True:
        sequence: str = input(txt)
        for s in sequence:
            if s not in "wsadWSAD":
                print("Neplatný postup")
                continue
        else:
            return sequence


def time_check(seq: str) -> bool:
    if len(seq) != 12:
        print("Špatná délka postupu!")
        return False
    for se in seq:
        if se not in "wsadWSAD":
            print("Neplatný postup")
            return False
    sequence: str = seq.lower()

    pos: list[int] = [0, 0]
    route_list: list[list[tuple[int, int]]] = []
    for seg in sequence:
        pos_new: list[int] = pos.copy()
        if seg == "w":
            pos_new[1] += 1
        elif seg == "s":
            pos_new[1] -= 1
        elif seg == "a":
            pos_new[0] -= 1
        elif seg == "d":
            pos_new[0] += 1
        route_list.append([tuple(pos), tuple(pos_new)])
        pos = pos_new

    for route in route_list:
        if route_list.count(route) > 1 or route_list.count(route[::-1]) > 1:
            print("Repeating path!")
            return False

    # return check
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
