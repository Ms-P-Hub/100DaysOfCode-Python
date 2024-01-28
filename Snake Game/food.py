import random
from turtle import Turtle

class Food (Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(0.5,0.5)
        self.color("red")
        self.speed("fastest")
        x = random.randint(-250,250)
        y = random.randint(-250,250)
        self.goto(x,y)
        