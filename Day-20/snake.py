from turtle import Turtle
MOVE_DISTANCE = 40
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
class Snake:

    def __init__(self):
        self.size = []

        x = 0
        for i in range(3):
            snake_part = Turtle(shape='square')
            snake_part.shapesize(2, 2, 15)
            snake_part.pendown()
            snake_part.pencolor('white')
            snake_part.goto(x, 0)
            snake_part.color('purple')
            self.size.append(snake_part)
            x -= 20

    def move(self):
        for num in range(len(self.size) - 1, 0, -1):
            new_x = self.size[num - 1].xcor()
            new_y = self.size[num - 1].ycor()
            self.size[num].goto(new_x, new_y)
        self.size[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.size[0].heading() != DOWN:
            self.size[0].setheading(UP)

    def down(self):
        if self.size[0].heading() != UP:
            self.size[0].setheading(DOWN)

    def right(self):
        if self.size[0].heading() != LEFT:
            self.size[0].setheading(RIGHT)

    def left(self):
        if self.size[0].heading() != RIGHT:
            self.size[0].setheading(LEFT)

