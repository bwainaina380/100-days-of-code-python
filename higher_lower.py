from random import randint

def higher_lower_game():
    running_score = 0
    while True:
        randomly_selected_celebrities = celebrities_to_compare(game_data)
        winner_celebrity = more_famous_celebrity(randomly_selected_celebrities)
        show_options(randomly_selected_celebrities)
        player_answer = input("Who do you think is more famous? Type 'A', 'B' or 'Equal': ")
        did_player_get_answer = is_player_correct(winner_celebrity, player_answer)
        if did_player_get_answer:
            print("Congratulations! That's correct.")
            running_score = player_score(did_player_get_answer, running_score)
            print(f"Your score is: {running_score}\n")
            continue
        else:
            print("Oops! You made a booo booo. Better luck next time.")
            running_score = player_score(did_player_get_answer, running_score)
            print(f"Your score is: {running_score}\n")
            break

def celebrities_to_compare(celebrity_list):
    return [
        celebrity_list[randint(0, len(celebrity_list) - 1)],
        celebrity_list[randint(0, len(celebrity_list) - 1)]
    ]

game_data = [
    {
        "name": "Rihanna",
        "industry": "music",
        "followers": 150,
        "country": "United States"
    },
    {
        "name": "Linus Torvalds",
        "industry": "technology",
        "followers": 120,
        "country": "Finland"
    }
]

def show_options(two_celebrities):
    first_celebrity = two_celebrities[0]
    second_celebrity = two_celebrities[1]
    print(f"{first_celebrity['name']} in the {first_celebrity['industry']} industry from {first_celebrity['country']}\nvs\n{second_celebrity['name']} in the {second_celebrity['industry']} industry from {second_celebrity['country']}")

def more_famous_celebrity(two_celebrities):
    if two_celebrities[0]["followers"] > two_celebrities[1]["followers"]:
        return "A"
    elif two_celebrities[0]["followers"] < two_celebrities[1]["followers"]:
        return "B"
    else:
        return "Equal"

def is_player_correct(correct_answer, player_answer):
    if correct_answer == player_answer:
        return True
    else:
        return False

def player_score(is_correct_answer, current_score):
    if is_correct_answer:
        current_score = current_score + 1
    else:
        current_score = current_score - 1
    return current_score

higher_lower_game()