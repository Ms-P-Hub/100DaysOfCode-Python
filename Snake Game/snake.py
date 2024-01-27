from turtle import Turtle

POSITIONS = [(0, 0), (20, 0), (40, 0)]
DISTANCE = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


class Snake:
    def __init__(self):
        self.turtles = []
        self.create_snake()
        self.head = self.turtles[0]

    def create_snake(self):
        for i in POSITIONS:
            sage = Turtle("circle")
            sage.penup()
            sage.color("white")
            sage.goto(i)
            self.turtles.append(sage)

    def move(self):
        for i in range(len(self.turtles) - 1, 0, -1):
            self.turtles[i].goto(self.turtles[i - 1].xcor(), self.turtles[i - 1].ycor())
        self.head.forward(DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)
