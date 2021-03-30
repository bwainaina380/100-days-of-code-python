import random

options = [["Rock", "🕳"], ["Paper", "📃"], ["Scissors", "✂️"]]

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
computer_choice = random.randint(0, 2)

if player_choice < 0 or player_choice > 2:
    print("You typed an invalid number. You lose.")
elif player_choice == 1 and computer_choice == 2:
    print(f"You chose {options[player_choice][0]} {options[player_choice][1]}.\nThe computer chose {options[computer_choice][0]} {options[computer_choice][1]}.\nYou lose.")
elif player_choice == 0 and computer_choice == 1:
    print(f"You chose {options[player_choice][0]} {options[player_choice][1]}.\nThe computer chose {options[computer_choice][0]} {options[computer_choice][1]}.\nYou lose.")
elif player_choice == 2 and computer_choice == 0:
    print(f"You chose {options[player_choice][0]} {options[player_choice][1]}.\nThe computer chose {options[computer_choice][0]} {options[computer_choice][1]}.\nYou lose.")
elif player_choice == computer_choice:
    print(f"You chose {options[player_choice][0]} {options[player_choice][1]}.\nThe computer chose {options[computer_choice][0]} {options[computer_choice][1]}.\nDraw.")
else:
    print(f"You chose {options[player_choice][0]} {options[player_choice][1]}.\nThe computer chose {options[computer_choice][0]} {options[computer_choice][1]}.\nYou win.")

