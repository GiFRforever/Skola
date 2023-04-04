import random


def player_attack(player_stats, dragon_stats):
    # Ask player for move
    move = int(input("Choose your move: 1 for attack, 2 for defend "))

    # Calculate damage to dragon
    if move == 1:
        damage = max(0, player_stats[1] - dragon_stats["defense"])
        dragon_stats["health"] -= damage
        print("You attack the dragon and deal", damage, "damage!")
    elif move == 2:
        player_stats[2] += 2
        print("You defend yourself and increase your defense by 2!")

    # Check if dragon is still alive
    if dragon_stats["health"] <= 0:
        print("Congratulations, you have slain the dragon!")
        return False
    else:
        return True


def dragon_attack(player_stats, dragon_stats):
    # Calculate damage to player
    damage = max(0, dragon_stats["attack"] - player_stats[2])
    player_stats[0] -= damage

    # Print attack message
    print("The dragon attacks you and deals", damage, "damage!")

    # Check if player is still alive
    if player_stats[0] <= 0:
        print("The dragon has defeated you!")
        return False
    else:
        return True


def dragon_slayer(dragon_stats, player_stats):
    while True:
        # Player attacks
        if not player_attack(player_stats, dragon_stats):
            break

        # Dragon attacks
        if not dragon_attack(player_stats, dragon_stats):
            break


dragon_stats = {"health": 100, "attack": 10, "defense": 5}

player_stats = [100, 8, 7]


dragon_slayer(dragon_stats, player_stats)
