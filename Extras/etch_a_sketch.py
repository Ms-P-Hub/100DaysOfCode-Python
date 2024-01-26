from turtle import Turtle, Screen

sage = Turtle()


def move_forward():
    sage.forward(10)
    
def move_backward():
    sage.backward(10)
    
def turn_right():
    sage.right(10)
  
def turn_left():
    sage.left(10)

def clear():
    sage.clear()
    sage.penup()
    sage.home()
    sage.pendown()
    
screen = Screen()
screen.listen()
screen.onkeypress(key="w", fun=move_forward)
screen.onkeypress(key="s", fun=move_backward)
screen.onkeypress(key="a", fun=turn_left)
screen.onkeypress(key="d", fun=turn_right)
screen.onkeypress(key="c", fun=clear)

screen.exitonclick()
