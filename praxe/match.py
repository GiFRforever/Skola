from datetime import datetime
from itertools import permutations
from random import randint


class Player:
    def __init__(
        self,
        firstname,
        lastname,
        date_of_birth,
        height,
        weight,
        total_scored_goals=0,
        total_played_matches=0,
    ):
        self.firstname: str = firstname
        self.lastname: str = lastname
        self.date_of_birth: str = date_of_birth
        self.height: int = height
        self.weight: int = weight
        self.total_scored_goals: int = total_scored_goals
        self.total_played_matches: int = total_played_matches


class Team:
    def __init__(
        self,
        name,
        colors,
        date_of_creation=datetime.now(),
        total_played_matches=0,
        total_scored_goals=0,
        *players,
    ):
        self.name: str = name
        self.colors: str = colors
        self.date_of_creation: datetime = date_of_creation
        self.total_played_matches: int = total_played_matches
        self.total_scored_goals: int = total_scored_goals
        self.players: list = list(players)
        self.number_of_players: int = len(self.players)
        self.matches: list = []


class Match:
    team1: Team = Team("None", "None")
    team2: Team = Team("None", "None")
    score1: int = 0
    score2: int = 0
    required_number_of_players: int = 0
    winner: Team = Team("None", "None")

    def __init__(
        self, team1, team2, score1=0, score2=0, required_number_of_players=0
    ) -> None:
        self.team1: Team = team1
        self.team2: Team = team2
        self.score1: int = score1
        self.score2: int = score2
        self.required_number_of_players: int = required_number_of_players

    def play(self) -> None:
        if (
            self.team1.number_of_players != self.required_number_of_players
            or self.team2.number_of_players != self.required_number_of_players
        ):
            print("Not enough players!")
            return
        self.team1.matches.append(self)
        self.team2.matches.append(self)
        self.team1.total_played_matches += 1
        self.team2.total_played_matches += 1
        if self.score1 > self.score2:
            self.winner = self.team1
        elif self.score1 < self.score2:
            self.winner = self.team2
        self.team1.total_scored_goals += self.score1
        self.team2.total_scored_goals += self.score2


class League:
    def __init__(self, name, players_per_team, *players) -> None:
        self.name: str = name
        self.players_per_team: int = players_per_team
        self.players: list[Player] = list(players)
        self.number_of_players: int = len(self.players)
        self.teams: list[Team] = []
        for i in range(0, self.number_of_players, self.players_per_team):
            team_players: list[Player] = list(
                self.players[i : i + self.players_per_team]
            )
            self.teams.append(
                Team(f"Team {i}", "Red", datetime.now(), 0, 0, *team_players)
            )
        self.number_of_teams: int = len(self.teams)


class Tournament:
    def __init__(self, name, *teams) -> None:
        self.name: str = name
        self.teams: list[Team] = list(teams)
        self.number_of_teams: int = len(self.teams)
        self.matches: list[Match] = []

    def play(self) -> None:
        for match in list(permutations(self.teams, 2)):
            self.matches.append(
                Match(match[0], match[1], randint(0, 5), randint(0, 5), 2)
            )

        for match in self.matches:
            match.play()
            print(
                f"{match.team1.name:} \33[93m {match.score1} : {match.score2} \33[0m {match.team2.name}"
            )
            print(f"The winner is {match.winner.name}!\n")


Adam: Player = Player("Adam", "Adamovic", "1990-01-01", 180, 80)
Boris: Player = Player("Boris", "Borisovic", "1991-01-01", 180, 80)
Cecil: Player = Player("Cecil", "Cecilovic", "1992-01-01", 180, 80)
David: Player = Player("David", "Davidovic", "1993-01-01", 180, 80)
Egon: Player = Player("Egon", "Egonovic", "1994-01-01", 180, 80)
Filip: Player = Player("Filip", "Filipovic", "1995-01-01", 180, 80)
Goran: Player = Player("Goran", "Goranovic", "1996-01-01", 180, 80)
Hrvoje: Player = Player("Hrvoje", "Hrvojevic", "1997-01-01", 180, 80)
Ivan: Player = Player("Ivan", "Ivanovic", "1998-01-01", 180, 80)
Josip: Player = Player("Josip", "Josipovic", "1999-01-01", 180, 80)

league: League = League(
    "League", 2, Adam, Boris, Cecil, David, Egon, Filip, Goran, Hrvoje, Ivan, Josip
)

tournament: Tournament = Tournament("Tournament", *league.teams)

tournament.play()
