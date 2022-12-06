from turtle import Turtle, Screen
import random

def start():
    my_t = Turtle()
    my_screen = Screen()
    colors = ["Red", "Blue", "Black", "Green", "Yellow"]
    directions = [0, 90, 180, 270]
    for _ in range(30):
        my_t.forward(30)
        direction = random.randint(0, 3)
        my_t.setheading(directions[direction])

    my_screen.exitonclick()

