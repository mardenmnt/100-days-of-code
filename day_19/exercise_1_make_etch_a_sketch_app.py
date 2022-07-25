
from turtle import Turtle, Screen

billy = Turtle()
screen = Screen()


def move_forward():
    billy.forward(10)


def move_backward():
    billy.backward(10)


def move_left():
    billy.left(10)


def move_right():
    billy.right(10)


def clear_all():
    billy.reset()


screen.listen()     # Iniciate listening keys. Without this comand the keys won't work
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="c", fun=clear_all)

screen.exitonclick()
