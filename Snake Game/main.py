from turtle import Turtle, Screen

screen = Screen()
screen.setup(600, 600, 0, 0)
screen.bgcolor("black")
screen.title("Snake Game!")
screen.tracer(0)

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
    screen.update()
    for i in range(len(turtles)-1,0,-1):
        turtles[i].goto(turtles[i-1].xcor(),turtles[i-1].ycor())
    turtles[0].forward(20)  
    turtles[0].left(90)  
        
screen.exitonclick()
