from turtle import Turtle, Screen
import random

timmy = Turtle()
my_screen = Screen()
print(my_screen.canvheight)
timmy.shape('turtle')
timmy.color('black', 'aquamarine')
timmy.pen(pencolor="black", fillcolor="black", pensize=1, speed=32)
my_screen.colormode(255)
timmy.speed(10000)

# n = 3
# for j in range(7):
#     for i in range(n):
#         timmy.forward(100)
#         timmy.right(360/n)
#     n += 1
#     timmy.pencolor(int(random.randint(1, 255)), int(random.randint(1, 255)), int(random.randint(1, 255)))

# m = [0, 90, 270, 180]
# for i in range(500):
#         timmy.pencolor(int(random.randint(1, 255)), int(random.randint(1, 255)), int(random.randint(1, 255)))
#         timmy.color(int(random.randint(1, 255)), int(random.randint(1, 255)), int(random.randint(1, 255)))
#         n = int(random.choice(m))
#         timmy.right(n)
#         timmy.forward(10)

p=2
for i in range(180):
        timmy.pencolor(int(random.randint(1, 255)), int(random.randint(1, 255)), int(random.randint(1, 255)))
        timmy.color(int(random.randint(1, 255)), int(random.randint(1, 255)), int(random.randint(1, 255)))
        timmy.right(p)
        timmy.circle(150)
        # p+=0.05


my_screen.exitonclick()
