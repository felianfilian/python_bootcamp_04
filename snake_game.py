import turtle
from turtle import Screen
from snake_snake import Snake
from snake_food import Food
from snake_score import Score
import time


def start():
    my_s = Screen()
    my_s.setup(width=600, height=600)
    my_s.title("Snake")
    my_s.bgcolor("black")
    my_s.tracer(0)

    snake = Snake()
    food = Food()
    score = Score()

    my_s.listen()
    my_s.onkey(snake.snake_up, "w")
    my_s.onkey(snake.snake_right, "d")
    my_s.onkey(snake.snake_down, "s")
    my_s.onkey(snake.snake_left, "a")

    turtle.write("Score = 0", True, align="center")

    game_active = True
    while game_active:
        my_s.update()
        time.sleep(0.1)
        snake.move()

        # detect collission with food
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            score.increase_score()

        # detect wall
        if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
            score.game_over()
            game_active = False

        # detect tail collission

    my_s.exitonclick()