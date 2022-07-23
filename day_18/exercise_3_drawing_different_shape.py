
from turtle import Turtle, Screen
from random import random, choice

billy = Turtle()
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]


def shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        billy.forward(100)
        billy.left(angle)


for shape_side_n in range(3, 11):
    billy.color(choice(colours))
    shape(shape_side_n)





screen = Screen()
screen.exitonclick()