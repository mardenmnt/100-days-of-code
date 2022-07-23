
import turtle
from random import randint

billy = turtle.Turtle()
turtle.colormode(255)
billy.speed("fastest")


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    color = (r, g, b)
    return color


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        billy.color(random_color())
        billy.circle(100)
        billy.setheading(billy.heading() + size_of_gap)


draw_spirograph(5)

screen = turtle.Screen()
screen.exitonclick()
