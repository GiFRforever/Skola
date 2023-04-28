import random

player_stats = (100, 10, 6)
dragon_stats = (200, 12, 2)

print("Welcome to Dragon Slayer!")
print("You are about to face a mighty dragon in a battle to the death.")

while True:
    move = int(input("Choose your move: 1 for attack, 2 for defend "))

    if move == 1:
        damage = random.randint(1, player_stats[1])
        dragon_stats = (dragon_stats[0] - damage, dragon_stats[1], dragon_stats[2])
        print(f"You attack the dragon and deal {damage} damage!")
    elif move == 2:
        player_stats = (player_stats[0], player_stats[1], player_stats[2] + 2)
        print("You defend yourself and increase your defense by 2!")
    else:
        print("Invalid move! Please try again.")
        continue

    if dragon_stats[0] <= 0:
        print("Congratulations, you have slain the dragon and saved the kingdom!")
        break

    dragon_damage = random.randint(1, dragon_stats[1])
    player_stats = (player_stats[0] - dragon_damage, player_stats[1], player_stats[2])

    if player_stats[0] <= 0:
        print("You have been defeated by the dragon. Better luck next time!")
        break

    if dragon_damage > 0:
        print(f"The dragon attacks you and deals {dragon_damage} damage!")
    else:
        print("Dragon did a critical hit.  You are dead")
        break
