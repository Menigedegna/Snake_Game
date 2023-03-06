from turtle import Turtle
import time

MOVE_DISTANCE = 10
SQUARE_SIZE = 20
SQUARE_COLOR = "purple"


def create_square(position):
    """returns turtle square"""
    square = Turtle(shape="square")
    square.shapesize(0.5, 0.5, 0)
    square.color(SQUARE_COLOR)
    square.penup()
    square.goto(position)
    return square


class Snake:

    def __init__(self, screen, snake_size, snake_speed):
        self.screen = screen
        self.screen.tracer(0)
        self.snake_size = snake_size
        self.snake_speed = snake_speed
        self.snake = []
        self.create_snake()

    def create_snake(self):
        x = (0, 0)
        for _ in range(self.snake_size):
            square = create_square(x)
            x = (x[0] - SQUARE_SIZE, 0)
            self.snake.append(square)

    def move_left(self):
        if self.snake[0].heading() != 0:
            self.snake[0].setheading(180)

    def move_right(self):
        if self.snake[0].heading() != 180:
            self.snake[0].setheading(0)

    def move_up(self):
        if self.snake[0].heading() != 270:
            self.snake[0].setheading(90)

    def move_down(self):
        if self.snake[0].heading() != 90:
            self.snake[0].setheading(270)

    def move_snake(self):
        time.sleep(self.snake_speed)
        self.screen.update()
        '''move snake one square at a time'''
        for idx, square in enumerate(self.snake):
            current_position = square.position()
            # square.speed(snake_speed)
            if idx == 0:
                square.forward(MOVE_DISTANCE)
            else:
                square.goto(previous_position)
            previous_position = current_position
        self.screen.listen()
        self.screen.onkey(key="Up", fun=self.move_up)
        self.screen.onkey(key="Down", fun=self.move_down)
        self.screen.onkey(key="Left", fun=self.move_left)
        self.screen.onkey(key="Right", fun=self.move_right)

    def add_snake_size(self):
        self.snake_size += 1
        '''add a square at the end of snake '''
        last_square_position = self.snake[-1].position()
        x = (last_square_position[0]-SQUARE_SIZE, last_square_position[1])
        new_square = create_square(x)
        self.snake.append(new_square)
