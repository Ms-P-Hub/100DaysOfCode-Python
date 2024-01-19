from random import choice

deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_cards = []
computer_cards = []

def deal_card():
    return choice(deck)


def deal_player():
    player_cards.append(deal_card())


def deal_computer():
    computer_cards.append(deal_card())


def calculate_score(total):
    score = sum(total)
    
    if 11 in total:
        if score > 21:
            score = score - 10
            return score
    elif score == 21 :
        return 0
    
    return score

def play():
    deal_player()
    deal_player()
    deal_computer()
    deal_computer()
    print(f"Your cards: {player_cards}")
    print(f"Computer's first card: {computer_cards[0]}")
    
    deal = input("Type 'y' to get another card, type 'n' to pass: ").lower()
    if deal == 'y':
        another_round()
    else:
        
        
        
        
def another_round():
    deal_player()
    deal_computer()