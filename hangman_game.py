from random import randint

hangman_lives_left = 7 # counting the head, neck, torso, right arm, left arm, right leg, and left leg
word_list = ["avocado", "subaru", "jumbotron"]
target_word = word_list[randint(0, len(word_list) - 1)]
target_word_len = len(target_word)

print(f"The selected word is {target_word}")

while(hangman_lives_left > 0 and target_word_len > 0):
    guess = input("Guess a letter: ").lower()
    if guess not in target_word:
        hangman_lives_left -= 1
        print("Wrong")
    else:
        target_word_len -= 1
        print("Correct")

if hangman_lives_left > 0:
    print("You won!")
else:
    print("You lost. Your man was hanged!")