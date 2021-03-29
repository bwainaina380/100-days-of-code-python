print('''
----|------------|-----------|----
    |        --/ - \--       |
   -|---------|  o  |--------|-
              /\ _ /
           []/       \[]
''')

print("Welcome to Treasure Island. Your mission is to find the treasure. Type in one of the answers in single quotes to play.\n")

if input("You are at a crossroad. Do you want to go 'left' or 'right'? ").lower() == "right":
    print("Game Over.")
else:
    if input("\nYou come across a river. Will you 'swim' or 'wait' for the boat? ").lower() == "swim":
        print("Game Over.")
    else:
        if input("\nYou find a house with 3 doors. Which door do you go through? 'yellow', 'red', or 'blue'? ").lower() == "yellow":
            print("\nYou Win!\n")
        else:
            print("\nGame Over.\n")
        