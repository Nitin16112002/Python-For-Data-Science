import random

def monty_hall_game():
    doors = ["goat", "goat", "car"]

    # Shuffle the doors randomly
    random.shuffle(doors)

    # Player makes an initial choice
    player_choice = int(input("Choose a door (1, 2, or 3): ")) - 1

    # Monty opens a door with a goat behind it
    remaining_doors = [i for i in range(3) if i != player_choice and doors[i] == "goat"]
    monty_opens = random.choice(remaining_doors)

    print(f"Monty opens Door {monty_opens + 1}, revealing a goat.")

    # Player decides whether to stick with the initial choice or switch
    switch = input("Do you want to switch doors? (yes/no): ").lower()

    if switch == "yes":
        remaining_doors = [i for i in range(3) if i != player_choice and i != monty_opens]
        player_choice = remaining_doors[0]

    # Reveal the result
    print(f"You chose Door {player_choice + 1}.")
    if doors[player_choice] == "car":
        print("Congratulations! You won the car!")
    else:
        print("Sorry, you got a goat.")

# Run the game
monty_hall_game()
