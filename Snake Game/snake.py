from turtle import Turtle

POSITIONS = [(0, 0), (20, 0), (40, 0)]


class Snake:
    def __init__(self):
        self.turtles = []
        self.create_snake()

    def create_snake(self):
        for i in POSITIONS:
            sage = Turtle("circle")
            sage.penup()
            sage.color("white")
            sage.goto(i)
            self.turtles.append(sage)
            
    def move(self):
        for i in range(len(self.turtles)-1,0,-1):
            self.turtles[i].goto(self.turtles[i-1].xcor(),self.turtles[i-1].ycor())
        self.turtles[0].forward(20)  
        self.turtles[0].left(90)  