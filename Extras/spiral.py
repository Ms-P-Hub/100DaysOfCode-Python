from turtle import Turtle, Screen
import random

sage = Turtle()

sage.speed("fastest")

for j in range(0, 100):
    sage.circle(100)
    sage.setheading(sage.heading() + 10)


screen = Screen()
screen.exitonclick()
