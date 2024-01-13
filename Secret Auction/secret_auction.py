import os
from art import logo

print(logo)
bids = {}
another_bid = True

while another_bid:
    name = input("What is your name: ").capitalize()
    amount = input("What's your bid: R")
    
    bids[name] = amount
    
    more_bidders =  input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    if more_bidders == 'yes':
        another_bid = True
        os.system('clear')
    else:
        another_bid = False
