import colorgram as cg
import turtle as t
import random

def draw_painting(height, width):
    for _ in range(height):
        for _ in range(width):
            pass

def start():
    # color_list = cg.extract("hirst.jpg", 60)
    # color_palette = []
    # for color in color_list:
    #     r = color.rgb.r
    #     g = color.rgb.g
    #     b = color.rgb.b
    #     new_color = (r, g, b)
    #     color_palette.append(new_color)

    t.colormode(255)
    my_t = t.Turtle()

    my_t.penup()
    my_t.hideturtle()

    color_list = [(199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57), (222, 224, 227), (186, 158, 53), (6, 57, 83), (109, 67, 85), (113, 161, 175), (22, 122, 174), (64, 153, 138), (39, 36, 36), (76, 40, 48), (9, 67, 47), (90, 141, 53), (181, 96, 79), (132, 40, 42), (210, 200, 151), (141, 171, 155), (179, 201, 186), (172, 153, 159), (212, 183, 177), (176, 198, 203), (150, 115, 120), (202, 185, 190), (40, 72, 82), (46, 73, 62), (47, 66, 82), (115, 134, 139)]

    my_t.speed("fastest")

    my_t.setheading(225)
    my_t.forward(250)
    my_t.setheading(0)


    for _ in range(10):
        for _ in range(10):
            my_t.dot(20, random.choice(color_list))
            my_t.forward(50)
        my_t.setheading(90)
        my_t.forward(50)
        my_t.setheading(180)
        my_t.forward(500)
        my_t.setheading(0)

    screen = t.Screen()
    screen.exitonclick()

