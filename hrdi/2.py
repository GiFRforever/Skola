import random
from sys import stdout


def dragon_slayer(dragon_stats, player_stats):
    # global tahy
    dragon_health = dragon_stats["health"]
    dragon_attack = dragon_stats["attack"]
    dragon_defense = dragon_stats["defense"]

    player_health = player_stats[0]
    player_attack = player_stats[1]
    player_defense = player_stats[2]

    print("A fearsome dragon appears!")

    while True:
        print("Dragon's health:", dragon_health)
        print("Player's health:", player_health)
        print()

        # Player's turn
        print("Player's turn:")
        print("1. Attack")
        print("2. Defend")
        choice = input("Choose your move (1 or 2): ")

        if choice == "1":
            player_damage = player_attack - dragon_defense
            if player_damage > 0:
                dragon_health -= player_damage
                print("You deal", player_damage, "damage to the dragon!")
            else:
                print("Your attack is too weak to penetrate the dragon's defenses.")
        elif choice == "2":
            player_defense *= 2
            print("You brace yourself for the dragon's attack.")

        if dragon_health <= 0:
            # stdout.write(" ".join([str(x) for x in iii]))
            print("You have slain the dragon! Congratulations!")
            break

        # Dragon's turn
        print()
        print("Dragon's turn:")
        dragon_damage = dragon_attack - player_defense
        if dragon_damage > 0:
            player_health -= dragon_damage
            print("The dragon deals", dragon_damage, "damage to you!")
        else:
            print("The dragon's attack is too weak to penetrate your defenses.")

        if player_health <= 0:
            print("You have been defeated by the dragon. Game over.")
            break

        # Reset player's defense
        player_defense //= 2

        print()

        # Pause for dramatic effect
        input("Press enter to continue...")


dragon_stats = {"health": 100, "attack": 10, "defense": 5}

player_stats = (100, 8, 7)

dragon_slayer(dragon_stats, player_stats)

"""
from itertools import combinations

iii: tuple = (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)


def tahoun():
    global iii
    global tahy
    for tah in tahy:
        iii = tah
        for t in tah:
            yield t


tažík = tahoun()

input = lambda x: next(tažík)


def print(*args):
    pass


tahy = list(combinations([1, 2], 23))
while True:
    dragon_slayer(dragon_stats, player_stats)
    stdout.write(" ".join([str(x) for x in iii]))
"""
