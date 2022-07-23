
import turtle
from random import choice, randint

billy = turtle.Turtle()
turtle.colormode(255)


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    color = (r, g, b)
    return color


directions = [0, 90, 180, 270]

billy.pensize(10)
billy.speed(4)

for _ in range(100):
    billy.color(random_color())
    billy.forward(38)
    billy.setheading(choice(directions))

screen = turtle.Screen()
screen.exitonclick()
