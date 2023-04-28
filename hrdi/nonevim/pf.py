import random

player_hp = 100
dragon_hp = 100

print("You are facing a dragon! Defeat it to become a hero!")

while player_hp > 0 and dragon_hp > 0:
    print("\nYour HP:", player_hp)
    print("Dragon's HP:", dragon_hp)
    print("Choose your action:")
    print("1. Attack")
    print("2. Defend")

    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        # player attacks
        damage = int(random.randint(10, 20) * (0.5 + player_hp / 200))
        dragon_hp -= damage
        print("You dealt", damage, "damage to the dragon!")
        # dragon attacks
        damage = int(random.randint(10, 20) * (0.5 + dragon_hp / 200))
        player_hp -= damage
        print("The dragon dealt", damage, "damage to you!")
    elif choice == "2":
        damage = int(random.randint(5, 10) * (0.5 + dragon_hp / 200))
        player_hp -= damage
        print("You defended and took only", damage, "damage from the dragon!")
    else:
        print("Invalid choice. Try again.")


if player_hp <= 0:
    print("\nYou have been defeated by the dragon. Game over.")
else:
    print("\nCongratulations! You have defeated the dragon and become a hero!")
