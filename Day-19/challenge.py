
from turtle import Turtle, Screen
import random
timmy = Turtle()
screen = Screen()
screen.listen()


def move_forwards():
    timmy.pencolor(int(random.randint(1, 255)), int(random.randint(1, 255)), int(random.randint(1, 255)))
    timmy.color(int(random.randint(1, 255)), int(random.randint(1, 255)), int(random.randint(1, 255)))
    timmy.forward(15)


def move_backwards():
    timmy.pencolor(int(random.randint(1, 255)), int(random.randint(1, 255)), int(random.randint(1, 255)))
    timmy.color(int(random.randint(1, 255)), int(random.randint(1, 255)), int(random.randint(1, 255)))
    timmy.forward(-15)


def turn_clockwise():
    timmy.right(10)


def turn_counter_clockwise():
    timmy.left(10)


def clear():
    timmy.penup()
    timmy.clear()
    timmy.goto(0, 0)
    timmy.pendown()


screen.onkey(key='w', fun=move_forwards)
screen.onkey(key='s', fun=move_backwards)
screen.onkey(key='d', fun=turn_clockwise)
screen.onkey(key='a', fun=turn_counter_clockwise)
screen.onkey(key='c', fun=clear)

print(screen.canvheight)
timmy.shape('turtle')

timmy.color('black', 'aquamarine')
timmy.pen(pencolor="black", fillcolor="black", pensize=5, speed=32)
screen.colormode(255)

screen.exitonclick()

