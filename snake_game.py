from turtle import Turtle, Screen

my_s = Screen()
my_s.setup(width=600, height=600)
my_s.title("Snake")
my_s.bgcolor("black")

segment_01 = Turtle("square")
segment_01.color("white")

segment_02 = Turtle("square")
segment_02.color("white")
segment_02.goto(-20, 0)

segment_03 = Turtle("square")
segment_03.color("white")
segment_03.goto(-40, 0)

def snake_up():
    print("test")
    segment_01.setheading(90)
    segment_01.forward(20)
def snake_right():
    pass
def snake_down():
    pass
def snake_left():
    pass


def start():
    my_s.listen()
    my_s.onkey(snake_up, "w")
    my_s.onkey(snake_right, "d")
    my_s.onkey(snake_down, "s")
    my_s.onkey(snake_left, "a")

    my_s.exitonclick()