from turtle import Screen, Turtle
import pandas as pd

score = 0

game = Turtle()
game.penup()
game.hideturtle()

screen = Screen()
screen.setup(725, 491)
screen.bgpic("./U.S. States Game/blank_states_img.gif")
screen.title("U.S. States Game")

data = pd.read_csv("./U.S. States Game/50_states.csv")
states = data.state.to_list()

guessed_states = []

is_game_on = True

while is_game_on:
    user_input = screen.textinput(
        f"{score}/{len(states)} States Correct", "What's another state name?"
    ).title()

    if user_input in states:
        guessed_states.append(user_input)
        score += 1
        x = int(data[data.state == user_input].x)
        y = int(data[data.state == user_input].y)
        game.goto(x, y)
        game.write(user_input, move=False, font=("Arial", 8, "normal"))
        
    elif user_input == "Exit" or score == len(states):
        is_game_on = False
        missed_states = [state for state in states if state not in guessed_states]
        
data = pd.DataFrame(missed_states, columns=["Missed States"])
print(data)