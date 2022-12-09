from turtle import Turtle, Screen
import time

my_s = Screen()
my_s.setup(width=600, height=600)
my_s.title("Snake")
my_s.bgcolor("black")
my_s.tracer(0)

start_pos = [(0, 0), (-20, 0), (-40, 0) ]
segments = []

game_active = True

for pos in start_pos:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(pos)
    segments.append(new_segment)

while game_active:
    my_s.update()
    time.sleep(0.1)
    for seg in range(len(segments) - 1, 0, -1):
        new_x = segments[seg -1].xcor()
        new_y = segments[seg - 1].ycor()
        segments[seg].goto(new_x, new_y)
    segments[0].forward(20)



def snake_up():
    print("test")

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