from scoreboard import Score
from turtle import Screen
from snake import Snake
from food import Food
import turtle


screen = Screen()
screen.setup(600, 600, 0, 0)
screen.bgcolor("black")
screen.title("Snake Game!")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

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
        score.add_score()
        food.refresh()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280:
        score.game_over()
        is_game_on = False
    elif snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.game_over()
        is_game_on = False

screen.exitonclick()
