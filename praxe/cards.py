from random import randint
from time import sleep
import sys, platform, os

# čištění konzole
if (p := platform.uname()[0]) == "Windows":
    clear = lambda: os.system("cls")

    def clean(n) -> None:
        for _ in range(n):
            sys.stdout.write("\033[F")
            sys.stdout.write("\033[K")

    def clean2(n) -> None:
        sys.stdout.write("\033[F")
        print(" " * n, end="\r")

elif p == "Linux":
    clear = lambda: os.system("clear")

    def clean(n) -> None:
        for _ in range(n):
            sys.stdout.write("\x1b[1A")
            sys.stdout.write("\x1b[2K")

    def clean2(n) -> None:
        sys.stdout.write("\x1b[1A")
        print(" " * n, end="\r")

else:
    clear = lambda: None

    def clean(n) -> None:
        pass

    def clean2(n) -> None:
        pass


def shuffle(deck: list) -> None:
    for i in range(len(deck)):
        j: int = randint(0, len(deck) - 1)
        deck[i], deck[j] = deck[j], deck[i]


def input_int_min_max(text: str, min: int, max: int) -> int:
    while True:
        try:
            number: int = int(input(text))
            if number >= min and number <= max:
                return number
            else:
                clean(1)
                print(f"Please enter a number between {min} and {max}.")
                sleep(3)
                clean(1)
        except ValueError:
            clean(1)
            print("Please enter a number.")
            sleep(3)
            clean(1)


class Card:
    VOCAB: dict[int, str] = {
        1: "Ace",
        11: "Jack",
        12: "Queen",
        13: "King",
    }

    def __init__(self, value, color) -> None:
        self.value = value
        self.color = color

    def __str__(self) -> str:
        return f"{self.VOCAB[self.value] if self.value in self.VOCAB else self.value} of {self.color}"


class Deck:
    CLUBS: str = "Clubs"
    DIAMONDS: str = "Diamonds"
    HEARTS: str = "Hearts"
    SPADES: str = "Spades"
    COLORS: tuple = (CLUBS, DIAMONDS, HEARTS, SPADES)

    def __init__(self, empty=False) -> None:
        if empty:
            self.cards: list[Card] = []
        else:
            self.reset_deck()
            self.shuffle()

    def reset_deck(self) -> None:
        self.cards: list[Card] = [
            Card(value, color)
            for value in [1] + list(range(7, 14))
            for color in self.COLORS
        ]

    def shuffle(self) -> None:
        shuffle(self.cards)

    def draw(self) -> Card:
        return self.cards.pop()

    def __str__(self) -> str:
        return f"Deck of {len(self.cards)} cards"

    def __add__(self, other) -> "Deck":
        if isinstance(other, Card):
            self.cards.append(other)
            return self
        elif isinstance(other, Deck):
            new_deck: Deck = Deck()
            new_deck.cards = other.cards + self.cards
            return new_deck
        else:
            raise TypeError(f"Can't add Deck and {type(other)} together.")

    def __radd__(self, other) -> "Deck":
        return self.__add__(other)


class Player:
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.hand: list[Card] = []
        self.game: Game

    def draw(self) -> None:
        if self.game == None:
            raise AttributeError("Player has no game to draw from.")
        if len(self.game.dealing_deck.cards) == 0:
            self.game.dealing_deck = self.game.throwing_deck
            self.game.throwing_deck = Deck(empty=True)
            self.game.throwing_deck += self.game.dealing_deck.draw()
            # self.game.dealing_deck.shuffle()
        self.hand.append(self.game.dealing_deck.draw())

    def __str__(self) -> str:
        return f"{self.name} has {len(self.hand)} cards"

    def show_hand(self) -> None:
        print(
            *[f"{i:>2}: {n}" for i, n in enumerate(self.hand, start=1)],
            sep="\n",
        )

    def play(self, card: Card) -> bool:
        if self.game == None:
            raise AttributeError("Player has no game to play in.")
        if self.game.card_is_playable(card):
            self.hand.remove(card)
            self.game.throwing_deck += card
            return True
        else:
            return False

    def suggestion(self) -> Card:
        if self.game == None:
            raise AttributeError("Player has no game to suggest in.")
        master_points: list[int] = []
        for card in self.hand:
            if self.game.card_is_playable(card):
                other_cards: list[Card] = self.hand.copy()
                other_cards.remove(card)
                other_cards_points: list[int] = []

                points: int = self.suggestion_recurse(
                    card, other_cards, other_cards_points
                )
                master_points.append(points)
            else:
                master_points.append(0)
        return self.hand[master_points.index(max(master_points))]

    def suggestion_recurse(
        self, card: Card, other_cards: list[Card], points: list[int]
    ) -> int:
        if len(other_cards) == 0:
            return sum(points)
        else:
            other_card: Card = other_cards.pop()
            if other_card.color == card.color:
                points.append(2)
            elif other_card.value == card.value:
                points.append(1)
            else:
                points.append(0)
            return self.suggestion_recurse(card, other_cards, points)

    def __add__(self, other) -> "Player":
        if isinstance(other, Card):
            self.hand.insert(0, other)
            return self
        else:
            raise TypeError(f"Can't add Player and {type(other)} together.")


class Game:
    def __init__(self, name, cards_per_player: int, *players) -> None:
        self.dealing_deck: Deck = Deck()
        self.throwing_deck: Deck = Deck(empty=True)
        # self.throwing_deck += self.dealing_deck.draw()
        self.name: str = name
        self.cards_per_player: int = cards_per_player
        self.players: list[Player] = list(players)
        self.winner: Player = Player("No one")
        self.draw_over: int = 0
        self.finale_order: list[Player] = []
        self.new_color: str = ""
        for player in self.players:
            player.game = self

    def deal(self) -> None:
        for _ in range(self.cards_per_player):
            for player in self.players:
                player.draw()
        self.throwing_deck += self.dealing_deck.draw()

    def card_is_playable(self, card: Card) -> bool:
        if len(self.throwing_deck.cards) == 0:
            return True
        elif self.throwing_deck.cards[-1].value == 7:
            # self.draw_over += 2
            return card.value == 7
        # elif self.throwing_deck.cards[-1].value == 1:
        #     return card.value == 1
        elif card.value == 12:
            return True
        else:
            if self.new_color == "":
                return (
                    card.color == self.throwing_deck.cards[-1].color
                    or card.value == self.throwing_deck.cards[-1].value
                )
            else:
                return (
                    card.color == self.new_color
                    or card.value == self.throwing_deck.cards[-1].value
                )

    def __str__(self) -> str:
        return f"{self.name} with {len(self.players)} players"

    def play(self) -> None:
        clear()
        self.deal()
        active_players: list[Player] = self.players.copy()
        finished_players: list[Player] = []
        active_skip: bool = False

        while len(active_players) > 1:
            for player in active_players:
                # last card check
                if self.draw_over:  # 7
                    if not any(map(lambda x: (x.value == 7), player.hand)):
                        print(f"You are drawing {self.draw_over} cards.")
                        for _ in range(self.draw_over):
                            player.draw()
                        self.draw_over = 0
                        continue
                elif len(player.hand) == 0:
                    active_players.remove(player)
                    finished_players.append(player)
                    print(f"{player.name} has finished.")
                    continue
                elif active_skip:  # ace
                    if not any(map(lambda x: (x.value == 1), player.hand)):
                        print("You are skipping your turn.")
                        active_skip = False
                        continue

                input(f"{player.name}'s turn. Press enter to continue.")
                clear()

                # show throwing deck
                print(f"Last card: {self.throwing_deck.cards[-1]}")
                if self.new_color != "":
                    print(f"New color: {self.new_color}")

                made_mistake: bool = True
                print("Your hand:")
                player.show_hand()
                print(" 0: Draw a card (skip your turn)")

                while made_mistake:
                    try:
                        card_index: int = input_int_min_max(
                            "Which card do you want to play?", 0, len(player.hand)
                        )
                        if card_index == 0:
                            if active_skip:
                                active_skip = False
                                break
                            for _ in range(self.draw_over + 1):
                                player.draw()
                            made_mistake = False
                        elif card_index > 0:
                            card: Card = player.hand[card_index - 1]
                            if self.card_is_playable(card):
                                if card.value == 7:
                                    self.draw_over += 2
                                elif card.value == 1:
                                    active_skip = True
                                elif card.value == 12:
                                    print("You are changing the color.")
                                    print(
                                        *[
                                            f"{i}: {color}"
                                            for i, color in enumerate(
                                                self.dealing_deck.COLORS, start=1
                                            )
                                        ],
                                        sep="\n",
                                    )
                                    players_choice: int = input_int_min_max(
                                        "Which color do you want to change to? ",
                                        1,
                                        4,
                                    )
                                    self.new_color = self.dealing_deck.COLORS[
                                        players_choice - 1
                                    ]
                                self.throwing_deck += card
                                player.hand.remove(card)
                                made_mistake = False
                            else:
                                print("You can't play that card.")
                        else:
                            print("Invalid input.")
                    except ValueError:
                        print("Invalid input.")
                clear()


"""
    def play(self) -> None:
        clear()
        self.deal()
        playing_players: list[Player] = self.players.copy()
        finished_players: list[Player] = []
        should_skip: bool = False
        while len(playing_players) > 1:
            for player in playing_players:
                if len(self.throwing_deck.cards) != 0:
                    if self.draw_over:  # 7
                        if any(
                            map(lambda x: x != 7, [card.value for card in player.hand])
                        ):
                            print(f"You are drawing {self.draw_over} cards.")
                            for _ in range(self.draw_over):
                                player.draw()
                            self.draw_over = 0
                            continue
                    # elif self.throwing_deck.cards[-1].value == 1:  # eso
                    elif should_skip:
                        if any(
                            map(lambda x: x != 1, [card.value for card in player.hand])
                        ):
                            print(f"({player.name}) is skipping their turn!\n")
                            sleep(5)
                            should_skip = False
                            continue
                    elif len(player.hand) == 0:  # winners
                        playing_players.remove(player)
                        finished_players.append(player)
                        continue

                print(f"Last card: {self.throwing_deck.cards[-1]}") if len(
                    self.throwing_deck.cards
                ) > 0 else print("You can play any card.")
                if self.new_color != "":
                    print(f"New color is {self.new_color}.")
                    self.new_color = ""

                made_mistake: bool = True
                player.show_hand()
                print(" 0: Draw a card ")
                while made_mistake:
                    players_choice: int = input_int_min_max(
                        "Which card do you want to play? ", 0, len(player.hand)
                    )
                    if players_choice:
                        card: Card = player.hand[players_choice - 1]
                        made_mistake = not player.play(card)
                        if made_mistake:
                            print(f"You can't play {card}.")
                            sleep(3)
                            clean(2)
                        elif card.value == 12:
                            print("You are changing the color.")
                            print(
                                *[
                                    f"{i}: {color}"
                                    for i, color in enumerate(
                                        self.dealing_deck.COLORS, start=1
                                    )
                                ],
                                sep="\n",
                            )
                            players_choice = input_int_min_max(
                                "Which color do you want to change to? ",
                                1,
                                4,
                            )
                            self.new_color = self.dealing_deck.COLORS[
                                players_choice - 1
                            ]
                        elif (
                            self.throwing_deck.cards[-1].value != 7 and card.value == 7
                        ):
                            self.draw_over += 2
                        elif card.value == 1:
                            should_skip = True
                    else:
                        player.draw()
                        made_mistake = False
                clear()
        else:
            self.winner = finished_players[0]
            print(f"{self.winner.name} won!")
            sleep(3)
            print(
                *[
                    f"{i}. place: {player.name}"
                    for i, player in enumerate(finished_players, start=2)
                ]
            )
            print(f"{playing_players[0].name} lost!")
            self.finale_order = finished_players + playing_players
"""


def create_game() -> Game:
    clear()
    print("Creating a new game.")
    name: str = input("Name of the game: ")
    players: list[Player] = []
    while True:
        player_name: str = input("Name of the player (empty to stop adding players): ")
        if player_name == "":
            break
        else:
            players.append(Player(player_name))
    cards_per_player: int = input_int_min_max(
        "How many cards should each player have? ", 1, 32 // len(players) - 1
    )
    return Game(name, cards_per_player, *players)


create_game().play()
