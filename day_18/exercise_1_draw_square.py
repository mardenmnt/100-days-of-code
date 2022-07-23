
from turtle import Turtle, Screen

billy = Turtle()

for _ in range(4):
    billy.forward(100)
    billy.left(90)

screen = Screen()
screen.exitonclick()
