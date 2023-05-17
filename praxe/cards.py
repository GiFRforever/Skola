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

    def __eq__(self, other) -> bool:
        if isinstance(other, Card):
            return self.value == other.value and self.color == other.color
        elif isinstance(other, int):
            return self.value == other
        else:
            raise TypeError(f"Can't compare Card and {type(other)} together.")

    def __gt__(self, other) -> bool:
        if isinstance(other, Card):
            return self.color == other.color
        else:
            raise TypeError(f"Can't compare Card and {type(other)} together.")

    def __lt__(self, other) -> bool:
        if isinstance(other, Card):
            return self.value == other.value
        else:
            raise TypeError(f"Can't compare Card and {type(other)} together.")


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
    def __init__(self, name: str, human: bool = True) -> None:
        self.name: str = name
        self.hand: list[Card] = []
        self.game: Game
        self.human: bool = human

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

    def suggest_card(self) -> int:
        points: list[int] = []
        for card in self.hand:
            if not self.game.card_is_playable(card):
                points.append(0)
                continue

            temp_cards: list[Card] = self.hand.copy()
            temp_cards.remove(card)
            points.append(self.suggest_recursion(temp_cards, card))

        return points.index(max(points)) if any(points) else -1

    def suggest_recursion(self, cards: list[Card], previous_card=None) -> int:  # type: ignore
        previous_card: Card = previous_card or cards.pop(0)
        temp_sum: int = 0 if previous_card == 12 else 1
        for card in cards:
            if not (previous_card > card or previous_card < card):
                continue
            temp_cards: list[Card] = cards.copy()
            temp_cards.remove(card)
            if card == 12:  # Queen
                temp_sum += self.suggest_recursion(temp_cards) + 1
            else:
                next_card: Card = temp_cards.pop(0)
                if card > next_card:
                    temp_sum += self.suggest_recursion(temp_cards) + 2
                elif card < next_card:
                    temp_sum += self.suggest_recursion(temp_cards)
        else:
            return temp_sum

    def suggest_color(self, cards: list[Card]) -> int:
        i: int = self.suggest_card()
        if i == -1:
            return 0
        return cards[i].color

    def __add__(self, other) -> "Player":
        if isinstance(other, Card):
            self.hand.insert(0, other)
            return self
        else:
            raise TypeError(f"Can't add Player and {type(other)} together.")

    def __sub__(self, other) -> list[Card]:
        if isinstance(other, Card):
            self.hand.remove(other)
            return self.hand
        else:
            raise TypeError(f"Can't subtract Player and {type(other)} together.")


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
        elif self.throwing_deck.cards[-1] == 7 and self.draw_over:
            # self.draw_over += 2
            return card == 7
        # elif self.throwing_deck.cards[-1].value == 1:
        #     return card.value == 1
        elif card == 12:
            return True
        else:
            if self.new_color == "":
                return (
                    card > self.throwing_deck.cards[-1]
                    or card < self.throwing_deck.cards[-1]
                )
            else:
                return (
                    card.color == self.new_color or card < self.throwing_deck.cards[-1]
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
                input(f"{player.name}'s turn. Press enter to continue.")
                clear()

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

                # show throwing deck
                print(f"Last card: {self.throwing_deck.cards[-1]}")
                if self.new_color != "":
                    print(f"New color: {self.new_color}")

                made_mistake: bool = True
                print("Your hand:")
                player.show_hand()
                print(" 0: Draw a card (skip your turn)")

                while made_mistake:
                    card_index: int = (
                        input_int_min_max(
                            "Which card do you want to play? ", 0, len(player.hand)
                        )
                        if player.human
                        else player.suggest_card() + 1
                    )
                    if card_index == 0:
                        if active_skip:
                            active_skip = False
                            break
                        for _ in range(self.draw_over + 1):
                            player.draw()
                        else:
                            self.draw_over = 0
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
                                players_choice: int = (
                                    input_int_min_max(
                                        "Which color do you want to change to? ",
                                        1,
                                        4,
                                    )
                                    if player.human
                                    else player.suggest_color(player - card)
                                )
                                self.new_color = (
                                    self.dealing_deck.COLORS[players_choice - 1]
                                    if players_choice
                                    else ""
                                )
                            self.throwing_deck += card
                            player.hand.remove(card)
                            made_mistake = False
                            self.new_color = ""
                        else:
                            print("You can't play that card.")
                    else:
                        print("Invalid input.")
                clear()


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
            players.append(
                Player(player_name, human=(False if "Ai" in player_name else True))
            )
    cards_per_player: int = input_int_min_max(
        "How many cards should each player have? ", 1, 32 // len(players) - 1
    )
    return Game(name, cards_per_player, *players)


create_game().play()
