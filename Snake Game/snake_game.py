from turtle import Turtle, Screen

screen = Screen()
screen.setup(600, 600, 0, 0)
screen.bgcolor("black")
screen.title("Snake Game!")

position = [(0, 0), (20, 0), (40, 0)]
turtles = []

for i in position:
    sage = Turtle("circle")
    sage.penup()
    sage.color("white")
    sage.goto(i)
    turtles.append(sage)

is_game_on = True

while is_game_on:
    for i in turtles:
        i.forward(20)

screen.exitonclick()
