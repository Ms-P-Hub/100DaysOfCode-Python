from turtle import Turtle, Screen
from snake import Snake


screen = Screen()
screen.setup(600, 600, 0, 0)
screen.bgcolor("black")
screen.title("Snake Game!")
screen.tracer(0)

snake = Snake()

is_game_on = True

while is_game_on:
    screen.update()
    snake.move()
        
screen.exitonclick()
