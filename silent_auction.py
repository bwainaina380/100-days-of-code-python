import math

print("Welcome to the secret auction program.")

auction_data = {}
more_bids = True

while(more_bids):
    name = input("What is your name? ")
    bid = int(input("What is your bid? $"))
    auction_data[name] = bid
    allow_another_bidder = input("\nAllow another bidder to bid? Type 'yes' or 'no': ").lower()
    if allow_another_bidder == "no":
        more_bids = False

def max_bid(bids_dictionary):
    max_bid = 0 
    winner = {}
    for bid in bids_dictionary:
        if bids_dictionary[bid] > max_bid:
            max_bid = bids_dictionary[bid]
            winner = {bid: max_bid}
    return winner

print(f"\nHere are all the auctions placed: {auction_data}")
print(f"The auction winner is: {max_bid(auction_data)}")