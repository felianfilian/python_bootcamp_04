import colorgram as cg

def draw_painting(height, width):
    pass

def start():
    color_list = cg.extract("hirst.jpg", 60)
    color_palette = []
    for color in color_list:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        new_color = (r, g, b)
        color_palette.append(new_color)

    print(color_palette)
