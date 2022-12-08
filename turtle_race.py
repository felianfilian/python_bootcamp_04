import random
from turtle import Turtle, Screen


def start():
    my_t = Turtle()
    my_s = Screen()
    my_s.setup(width=500, height=400)
    user_bet = my_s.textinput(title="Your bet", prompt="Which turtle will wim the race? Enter a color: ")

    colors = ["red", "blue", "orange", "green", "purple"]
    all_turtles = []
    race_active = True

    for turtle_idx in range(5):
        new_turtle = Turtle(shape="turtle")
        new_turtle.color(colors[turtle_idx])
        new_turtle.penup()
        new_turtle.goto(x=-230, y=-100 + (turtle_idx * 50))
        all_turtles.append(new_turtle)

    if user_bet:
        race_active = True

    while race_active:
        for turtle in all_turtles:
            if turtle.xcor() > 230:
                race_active = False
                win_color = turtle.pencolor()
                print(f"{turtle.pencolor()} win the race")
                if win_color == user_bet:
                    print("you won the race!")
                else:
                    print("you lost")

            rand_distance = random.randint(0, 10)
            turtle.forward(rand_distance)


    my_s.exitonclick()
