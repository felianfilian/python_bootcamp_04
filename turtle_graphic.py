from turtle import Turtle, Screen


def start():
    my_t = Turtle()
    my_t.shape("turtle")
    my_screen = Screen()

    num_sides = int(input("Sides:\n"))

    for _ in range(num_sides):
        my_t.forward(50)
        my_t.left(360 / num_sides)


    my_screen.exitonclick()


