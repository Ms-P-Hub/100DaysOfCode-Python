from turtle import Screen
from paddle import Paddle
import turtle

screen = Screen()
screen.setup(800, 600, 0, 0)
screen.bgcolor("black")
screen.title("Pong!")

paddle = Paddle()

screen.listen()
screen.onkeypress(paddle.up,"Up")
screen.onkeypress(paddle.down,"Down")

screen.exitonclick()