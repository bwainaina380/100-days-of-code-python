from random import randint

def play_game():
    human_player = {"name": "You", "cards": []}
    computer_player = {"name": "Computer", "cards": []}
    deal_cards(human_player, 2)
    deal_cards(computer_player, 2)
    print_cards(human_player, computer_player)

    while True:
       get_another_card = input("Do you want another card? Type 'yes' or 'no': ")
       if get_another_card == "yes":
           deal_cards(human_player, 1)
           deal_cards(computer_player, 1)
           print_cards(human_player, computer_player)
           human_player_score = player_score(human_player)
           computer_player_score = player_score(computer_player)
           winner = get_winner(human_player, computer_player)
           print(winner)
           if next_step(human_player_score, computer_player_score) == "stop game":
               break
           else:
               continue
       else:
            print_cards(human_player, computer_player)
            print(get_winner(human_player, computer_player))
            break

def deal_cards(player, num_of_cards):
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    for _ in range(num_of_cards):
        delt_card = cards[randint(0, len(cards) - 1)]
        player["cards"].append(delt_card)

def print_cards(first_player, second_player):
    print("Your deck")
    print(first_player)
    print(second_player)

def get_winner(first_player, second_player):
    first_player_score = player_score(first_player)
    second_player_score = player_score(second_player)
    if first_player_score > 21 and second_player_score > 21:
        return "You both lost"
    elif first_player_score > 21:
        return f"{second_player['name']} wins"
    elif second_player_score > 21:
        return f"{first_player['name']} wins"
    if first_player_score == second_player_score:
        return "Draw"
    elif first_player_score == 21:
        return f"{first_player['name']} blackjack"
    elif second_player_score == 21:
        return f"{second_player['name']} blackjack"
    elif first_player_score > second_player_score:
        return f"{first_player['name']} wins"
    elif second_player_score > first_player_score:
        return f"{second_player['name']} wins"

def player_score(player):
    return sum(player["cards"])

def next_step(first_player_score, second_player_score):
    if first_player_score < 21 and second_player_score < 21:
        return
    else:
        return "stop game"

def fresh_shuffle():
    print("Fresh shuffle")

play_game()