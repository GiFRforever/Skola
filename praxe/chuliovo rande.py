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

    sequence: str = seq.lower()

    invalid_parts: list[str] = ["ws", "sw", "ad", "da"]
    for part in invalid_parts:
        if part in sequence:
            print("Repeating path!")
            return False

    # p check
    sequence_p: str = sequence
    for double, single in zip(["ww", "ss", "aa", "dd"], ["w", "s", "a", "d"]):
        while double in sequence_p:
            sequence_p = sequence_p.replace(double, single)
    # p_invalid_parts: list[str] = ["was", "saw", "wds", "sdw", "asd", "dsa", "aws", "swd"]
    p_invalid_parts: list[str] = [
        "wasd",
        "sawd",
        "wdsa",
        "sdaw",
        "asdw",
        "dsaw",
        "awsd",
        "swda",
    ]
    for part in p_invalid_parts:
        while part in sequence_p:
            sequence_p = sequence_p.replace(part, "")
    else:
        if (len(sequence_p) % 4) != 0:
            print("P-return!")
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
