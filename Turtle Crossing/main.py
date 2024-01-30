from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(600, 600)
screen.title("Turtle Crossing")
screen.tracer(0)

player = Player()
score = Scoreboard()

screen.listen()
screen.onkeypress(player.up, "Up")

is_game_on = True

while is_game_on:
    time.sleep(0.1)
    screen.update()

    if player.finished():
        score.increase_score()
        score.update_score()
        player.reset()


screen.exitonclick()
