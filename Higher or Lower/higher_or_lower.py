from art import logo , vs
from game_data import data
import random

def choice():
    return random.choice(data)

print(logo)
choice_1 = choice()
print(f"Compare A: {choice_1['name']}, {choice_1['description']} from {choice_1['country']}")

print(vs)
choice_2 = choice()
print(f"Compare B: {choice_2['name']}, {choice_2['description']} from {choice_2['country']}")