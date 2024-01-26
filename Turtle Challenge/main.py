from turtle import Turtle, Screen
import turtle
import random

sage = Turtle()
turtle.colormode(255)

colors = [
    (0, 0, 0),
    (23, 0, 142),
    (221, 0, 0),
    (253, 97, 47),
    (253, 245, 0),
    (0, 186, 0),
    (0, 155, 253),
    (253, 136, 35),
    (0, 118, 224),
    (254, 219, 8),
    (231, 30, 14),
    (128, 216, 0),
]

sage.hideturtle()
sage.penup()
sage.setheading(210)
sage.forward(250)
sage.setheading(0)
for i in range(8):
    for j in range(10):
        sage.dot(20, random.choice(colors))
        sage.penup()
        sage.forward(50)
    sage.penup()
    sage.setheading(90)
    sage.forward(50)
    sage.setheading(180)
    sage.forward(500)
    sage.setheading(0)

screen = Screen()
screen.exitonclick()
