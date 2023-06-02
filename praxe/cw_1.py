from random import randint


def points(games):  # type: ignore
    return sum(
        3 if left > right else 1 if left == right else 0
        for game in games
        for left, right in [map(lambda x: int(x), game.split(":"))]
    )


def random_tests():
    left: int = 0
    right: int = 0
    said: int = 0
    try:
        for _ in range(1000):
            left = randint(0, 1000)
            right = randint(0, 1000)
            assert (said := points([f"{left}:{right}"])) == (
                3 if left > right else 1 if left == right else 0
            )
    except AssertionError:
        print(f"Failed on {left}:{right}")
        print(f"Said: {said}")
    else:
        print("All tests passed")


random_tests()


def points(games):
    return sum([0, 1, 3][1 + (g[0] > g[2]) - (g[0] < g[2])] for g in games)


random_tests()
