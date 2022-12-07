from turtle import Turtle, Screen
import random

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

def draw_spiro(gap):
    my_t = Turtle()
    for _ in range(int(360 / gap)):
        my_t.speed("fastest")
        my_t.color(random_color())
        my_t.circle(100)
        my_t.setheading(my_t.heading() + gap)


def start():

    draw_spiro(5)

    my_screen = Screen()
    my_screen.exitonclick()