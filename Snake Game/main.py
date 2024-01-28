from food import Food
from snake import Snake
import turtle
from turtle import Screen


screen = Screen()
screen.setup(600, 600, 0, 0)
screen.bgcolor("black")
screen.title("Snake Game!")
screen.tracer(0)

snake = Snake()
food = Food()

screen.listen()

screen.onkeypress(snake.up, "Up")
screen.onkeypress(snake.down, "Down")
screen.onkeypress(snake.left, "Left")
screen.onkeypress(snake.right, "Right")


is_game_on = True

while is_game_on:
    screen.update()
    turtle.time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()

screen.exitonclick()
