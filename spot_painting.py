import colorgram as cg

def draw_painting(height, width):
    pass

def start():
    color_list = cg.extract("hirst.jpg", 60)
    print(color_list)
    color_palette = []

    for color in color_list:
        color_palette.append(color.tgb)

    print(color_palette)
