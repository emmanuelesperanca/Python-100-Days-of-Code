import colorgram
from turtle import Turtle, Screen
import random
timmy = Turtle()
my_screen = Screen()
print(my_screen.canvheight)
timmy.shape('circle')
timmy.shapesize(0.1,0.1,0.1)
timmy.color('black', 'aquamarine')
timmy.pen(pencolor="black", fillcolor="black", pensize=5, speed=32)
my_screen.colormode(255)
timmy.speed(10000)


colors = colorgram.extract('apgjo1W_700.jpg', 20)
rgbs=[]
for i in colors:
    rgbs.append(i.rgb)

y = -150
for i in range(10):
    timmy.penup()
    timmy.goto(-150, y)
    y += 30
    for i in range(10):
        timmy.pencolor(random.choice(rgbs))
        timmy.color(random.choice(rgbs))
        timmy.pendown()
        timmy.dot(30)
        timmy.penup()
        timmy.forward(30)

my_screen.exitonclick()

