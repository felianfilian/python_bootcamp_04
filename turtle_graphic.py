from turtle import Turtle, Screen


def start():
    my_t = Turtle()
    my_screen = Screen()

    for _ in range(10):
        my_t.penup()
        my_t.forward(10)
        my_t.pendown()
        my_t.forward(10)


    my_screen.exitonclick()


