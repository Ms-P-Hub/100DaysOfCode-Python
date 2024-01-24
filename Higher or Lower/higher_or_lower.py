from art import logo, vs
from game_data import data
import random
import os

score = 0


def choice():
    return random.choice(data)


def play():
    print(logo)
    choice_1 = choice()
    print(
        f"Compare A: {choice_1['name']}, a {choice_1['description']} from {choice_1['country']}"
    )

    print(vs)
    choice_2 = choice()
    print(
        f"Compare B: {choice_2['name']}, a {choice_2['description']} from {choice_2['country']}"
    )

    guess = input("Who has more followers? Type 'A' or 'B': ").upper()

    if choice_1["follower_count"] > choice_2["follower_count"]:
        answer = "A"
    elif choice_1["follower_count"] < choice_2["follower_count"]:
        answer = "B"

    if guess == answer:
        os.system("clear")
        global score
        score += 1
        print(f"You're right! current score:{ score}")
        play()
    else:
        os.system("clear")
        return print(f"Sorry, that's wrong. final score: {score}")


play()
