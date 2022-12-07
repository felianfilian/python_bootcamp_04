from turtle import Turtle, Screen


def start():
    my_t = Turtle()
    my_s = Screen()

    def move_forwards():
        my_t.forward(10)

    my_s.listen()
    my_s.onkey(move_forwards, "space")
    my_s.exitonclick()
