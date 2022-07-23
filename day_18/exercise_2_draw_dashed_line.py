
from turtle import Turtle, Screen

billy = Turtle()

for _ in range(10):
    billy.forward(15)
    billy.penup()
    billy.forward(10)
    billy.pendown()

screen = Screen()
screen.exitonclick()
