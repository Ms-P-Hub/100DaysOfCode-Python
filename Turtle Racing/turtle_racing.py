from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=400, height=400, startx=0, starty=0)
screen.title("Turtle Racing Game!")
bet = screen.textinput(
    title="Make your bet", prompt="Which color do you think will win the race?\n1. Yellow\n2. Blue\n3. Red\n4. Purple\n5. Black\n6. Cyan\n7. Green"
)

colors = ["yellow","blue","red","purple","cyan","green"]
start = 150
for i in range(6):
    sage = Turtle(shape="turtle")
    sage.color(colors[i])
    sage.penup()
    sage.goto(-150, start)
    start -= 50

screen.exitonclick()
