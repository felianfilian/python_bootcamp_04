import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)

def start():
    my_t = Turtle()
    my_screen = Screen()
    colors = ["Red", "Blue", "Black", "Green", "Cyan"]
    directions = [0, 90, 180, 270]
    for _ in range(70):
        my_t.speed("fastest")
        my_t.color(random_color())
        my_t.pensize(12)
        my_t.forward(30)
        my_t.setheading(random.choice(directions))

    my_screen.exitonclick()

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)
