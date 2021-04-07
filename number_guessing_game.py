from random import randint

print("""
 _____                        ___    _   _                 _               
|  __ \                      / _ \  | \ | |               | |              
| |  \/_   _  ___  ___ ___  / /_\ \ |  \| |_   _ _ __ ___ | |__   ___ _ __ 
| | __| | | |/ _ \/ __/ __| |  _  | | . ` | | | | '_ ` _ \| '_ \ / _ \ '__|
| |_\ \ |_| |  __/\__ \__ \ | | | | | |\  | |_| | | | | | | |_) |  __/ |   
 \____/\__,_|\___||___/___/ \_| |_/ \_| \_/\__,_|_| |_| |_|_.__/ \___|_|   

""")

def answer():
    return randint(0, 100)

def guess_too_high_or_low(answer, guess):
    if answer > guess:
        return "Too low"
    elif guess > answer:
        return "Too high"
    else:
        return "Correct"

def game():
    target_answer = answer()
    trials_left = 0
    hard_or_easy = input("Would you like to play the hard level or the easy level? Type 'hard' or 'easy': ")
    if hard_or_easy == "hard":
        trials_left = 5
    else:
        trials_left = 10

    while(trials_left > 0):
        guess = int(input("Guess a number: "))
        if guess_too_high_or_low(target_answer, guess) == "Correct":
            print(f"Correct! The answer is {target_answer}!")
            break
        else:
            print(guess_too_high_or_low(target_answer, guess))
            trials_left = trials_left - 1
            print(f"Number of guesses left: {trials_left}")
            continue
    
game()
        