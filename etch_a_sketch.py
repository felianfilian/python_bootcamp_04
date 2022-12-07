from turtle import Turtle, Screen


def start():
    my_t = Turtle()
    my_s = Screen()

    def move_forwards():
        my_t.forward(20)
    def move_backwards():
        my_t.back(20)
    def move_left():
        my_t.left(90)
        my_t.forward(20)

    def move_right():
        my_t.right(90)
        my_t.forward(20)

    my_s.listen()
    my_s.onkey(move_forwards, "w")
    my_s.onkey(move_backwards, "s")
    my_s.onkey(move_left, "a")
    my_s.onkey(move_right, "d")

    my_s.exitonclick()
