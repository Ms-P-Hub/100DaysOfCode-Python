from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=400, height=400, startx=0, starty=0)
screen.title("Turtle Racing Game!")
bet = screen.textinput(
    title="Make your bet",
    prompt="Which color do you think will win the race?\n1. Yellow\n2. Blue\n3. Red\n4. Purple\n5. Cyan\n7. Green",
)

colors = ["yellow", "blue", "red", "purple", "cyan", "green"]
all_turtles = []
start = 150
for i in range(6):
    sage = Turtle(shape="turtle")
    sage.color(colors[i])
    sage.penup()
    sage.goto(-150, start)
    start -= 50
    all_turtles.append(sage)

if bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 180:
            print(f"The {turtle.pencolor()} turtle has won!")
            if turtle.pencolor() == bet.lower():
                print(f"You have also won your bet!")
                is_race_on = False
            else:
                print(f"You have lost your bet!")
                is_race_on = False
        turtle.forward(random.randint(0, 10))


screen.exitonclick()
