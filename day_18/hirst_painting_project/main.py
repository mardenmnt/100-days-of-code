
import turtle
from turtle import Turtle, Screen
from random import choice

# import colorgram
#
# colors = colorgram.extract("image.jpg", 30)
#
# rgb_colors = []
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_colors.append((r, g, b))
#
# print(rgb_colors)

billy = Turtle()
billy.speed("fastest")
billy.penup()
billy.hideturtle()
turtle.colormode(255)

color_list = [(243, 251, 248), (252, 246, 250), (237, 244, 250), (32, 107, 148), (224, 154, 87), (213, 131, 158), (6, 52, 93), (118, 172, 194), (34, 132, 81), (148, 80, 31), (19, 169, 203), (207, 156, 18), (229, 210, 103), (138, 25, 44), (210, 90, 121), (141, 183, 166), (10, 100, 57), (13, 64, 126), (222, 213, 7), (11, 44, 35), (81, 81, 20), (224, 169, 192), (58, 51, 11), (138, 61, 85), (3, 89, 115), (168, 207, 187), (240, 171, 155), (72, 157, 107), (157, 25, 16)]

billy.setheading(225)
billy.forward(350)
billy.setheading(0)

number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    billy.dot(20, choice(color_list))
    billy.forward(50)
    billy.dot(20, choice(color_list))

    if dot_count % 10 == 0:
        billy.setheading(90)
        billy.forward(50)
        billy.setheading(180)
        billy.forward(500)
        billy.setheading(0)

screen = Screen()
screen.exitonclick()
