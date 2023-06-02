from math import factorial
from pprint import pprint


def is_in_round(team, master, round_number) -> bool:
    round = master[round_number]
    for game in round:
        if team in game:
            return True
    return False


def was_with_them(team1, team2, master):
    for round in master:
        for game in round:
            if team1 in game and team2 in game:
                return True
    return False


def create_tournament(number_of_teams: int):
    if number_of_teams < 2:
        raise ValueError("Number of teams must be at least 2")
    # if number_of_teams % 2 != 0:
    #     raise ValueError("Number of teams must be even")

    master: list[list[list[int]]] = [
        [[0, 0] for _ in range(number_of_teams // 2)]
        for _ in range(number_of_teams - 1)
    ]

    teams: list[int] = list(range(1, number_of_teams + 1))
    """
    master(4) = [
        [[1, 2], [3, 4]], <- 1st round, 2 games
        [[1, 3], [2, 4]],
        [[1, 4], [2, 3]],
        ]
    """

    for i, round in enumerate(master):
        for j, game in enumerate(round):
            # for side in range(len(game)):
            for t in teams:
                if is_in_round(t, master, i):
                    continue
                else:
                    game[0] = t
                    break
            for t in teams:
                if is_in_round(t, master, i) or t == game[0]:
                    continue
                elif was_with_them(t, game[0], master):
                    continue
                else:
                    game[1] = t
                    break

    return master


how_many_teams = 6

tournament = create_tournament(how_many_teams)
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
