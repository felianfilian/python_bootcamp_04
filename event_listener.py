import turtle as t


def start():
    def move_f():
        my_t.forward(10)

    my_t = t.Turtle()
    my_s = t.Screen()

    my_s.listen()
    my_s.onkey(key="space", fun=move_f)
    my_s.exitonclick()
