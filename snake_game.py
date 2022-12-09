from turtle import Turtle, Screen
from snake_snake import Snake
import time

def start():
    my_s = Screen()
    my_s.setup(width=600, height=600)
    my_s.title("Snake")
    my_s.bgcolor("black")
    my_s.tracer(0)

    snake = Snake()

    my_s.listen()
    my_s.onkey(snake.snake_up, "w")
    my_s.onkey(snake.snake_right, "d")
    my_s.onkey(snake.snake_down, "s")
    my_s.onkey(snake.snake_left, "a")

    game_active = True
    while game_active:
        my_s.update()
        time.sleep(0.1)
        snake.move()

    my_s.exitonclick()