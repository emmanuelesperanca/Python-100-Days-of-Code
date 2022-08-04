import time
from turtle import Turtle, Screen
from snake import Snake

screen = Screen()
screen.listen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.colormode(255)
screen.title('Snake Game')
screen.tracer(0)


snake = Snake()

screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.right, 'Right')
screen.onkey(snake.left, 'Left')


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()




screen.exitonclick()
