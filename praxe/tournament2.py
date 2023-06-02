from pprint import pprint
from itertools import permutations


def was_with_them(team1, team2, master):
    for round in master:
        for game in round:
            if team1 in game and team2 in game:
                return True
    return False


def circle_method(n) -> list[list[list[int]]]:
    """
    circle_method(4) = [
        [[1, 2], [3, 4]], <- 1st round, 2 games
        [[1, 3], [2, 4]],
        [[1, 4], [2, 3]],
        ]
    master: list[list[list[int]]] = [
        [[0, 0] for _ in range(n // 2)] for _ in range(n - 1)
    ]

    teams: list[int] = list(range(1, n + 1))

    for i, round in enumerate(master):
        for j, game in enumerate(round):
            # for side in range(len(game)):
            for t in teams:
                if t in game:
                    continue
                elif t in [g[0] for g in master[i]]:
                    continue
                elif was_with_them(t, game[0], master):
                    continue
                else:
                    game[1] = t
                    break
            for t in teams:
                if t in game:
                    continue
                elif t in [g[0] for g in master[i]]:
                    continue
                elif t in [g[1] for g in master[i]]:
                    continue
                elif was_with_them(t, game[0], master):
                    continue
                elif was_with_them(t, game[1], master):
                    continue
                else:
                    game[0] = t
                    break

    return master
    """
    # return permutations(2, [n for n in range(n)])


how_many_teams: int = 6

tournament: list[list[list[int]]] = circle_method(how_many_teams)
pprint(tournament)

for i in range(how_many_teams):
    i += 1
    for j in range(how_many_teams):
        j += 1
        if i == j:
            continue
        elif was_with_them(i, j, tournament):
            # print(f"{i} was with {j}")
            pass
        else:
            print(f"{i} was not with {j}")
