import os
from art import logo

print(logo)
bids = {}
another_bid = True

def find_highest_bidder(library):
    highest_amount = 0
    
    for key in bids:
        value = bids[key]
        if value > highest_amount:
            highest_amount = value
            highest_bidder = key
    
    print(f"The winner is {highest_bidder} with a bid of R{highest_amount}")

while another_bid:
    name = input("What is your name: ").capitalize()
    amount = int(input("What's your bid: R"))
    
    bids[name] = amount
    
    more_bidders =  input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    if more_bidders == 'yes':
        another_bid = True
        os.system('clear')
    else:
        another_bid = False
        find_highest_bidder(bids)


    