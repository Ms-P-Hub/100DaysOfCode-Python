from turtle import Screen
import turtle
from snake import Snake


screen = Screen()
screen.setup(600, 600, 0, 0)
screen.bgcolor("black")
screen.title("Snake Game!")
screen.tracer(0)

snake = Snake()

screen.listen()

screen.onkeypress(snake.up,"Up")
screen.onkeypress(snake.down,"Down")
screen.onkeypress(snake.left,"Left")
screen.onkeypress(snake.right,"Right")


is_game_on = True

while is_game_on:
    screen.update()
    turtle.time.sleep(0.1)
    snake.move()
        
screen.exitonclick()
