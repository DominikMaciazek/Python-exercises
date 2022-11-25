import turtle as turtle_module
import random

turtle_module.colormode(255)
domi = turtle_module.Turtle()
domi.speed("fastest")
domi.penup()
domi.hideturtle()
color_list = [(236, 224, 80), (197, 7, 71), (195, 164, 13), (201, 75, 15), (231, 54, 132), (110, 179, 216),
              (217, 163, 101), (27, 105, 168), (35, 186, 109), (19, 29, 168), (13, 23, 66), (212, 135, 177),
              (233, 223, 7), (199, 33, 132), (13, 183, 212), (230, 166, 199), (126, 189, 162), (8, 49, 28),
              (40, 132, 77), (128, 219, 232), (58, 12, 25), (67, 22, 7), (114, 90, 210), (146, 216, 199),
              (179, 17, 8), (233, 66, 34)]

domi.setheading(225)
domi.forward(300)
domi.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    domi.dot(20, random.choice(color_list))
    domi.forward(50)

    if dot_count % 10 == 0:
        domi.setheading(90)
        domi.forward(50)
        domi.setheading(180)
        domi.forward(500)
        domi.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()

# Extract RGB colors from JPG

# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('dots.jpg', 30)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)