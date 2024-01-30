from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

is_game_on = True

screen = Screen()
screen.setup(800, 600, 0, 0)
screen.bgcolor("black")
screen.title("Pong!")
screen.tracer(0)

right_paddle = Paddle(350, 0)
left_paddle = Paddle(-350, 0)
ball = Ball()

screen.listen()
screen.onkeypress(right_paddle.up, "Up")
screen.onkeypress(right_paddle.down, "Down")

screen.onkeypress(left_paddle.up, "w")
screen.onkeypress(left_paddle.down, "s")


while is_game_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

screen.exitonclick()
