from turtle import Turtle
import time

MOVE_DISTANCE = 10
SQUARE_SIZE = 20

class Snake:

    def __init__(self, screen, snake_size, snake_speed=1):
        self.screen = screen
        self.screen.tracer(0)
        self.snake_size = snake_size
        self.snake_speed = snake_speed
        self.snake = []
        self.create_snake()

    def create_snake(self):
        x = (0, 0)
        for _ in range(self.snake_size):
            square = Turtle(shape="square")
            square.shapesize(0.5, 0.5, 0)
            square.color("white")
            square.penup()
            square.goto(x)
            x = (x[0] - SQUARE_SIZE, 0)
            self.snake.append(square)

    def move_left(self):
        self.snake[0].setheading(180)

    def move_right(self):
        self.snake[0].setheading(0)

    def move_up(self):
        self.snake[0].setheading(90)

    def move_down(self):
        self.snake[0].setheading(270)

    def move_snake(self):
        time.sleep(self.snake_speed/10)
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
        new_square = Turtle(shape="square")
        new_square.shapesize(0.5, 0.5, 0)
        new_square.color("white")
        new_square.penup()
        last_square_position = self.snake[-1].position()
        new_square.goto(last_square_position[0]-SQUARE_SIZE, last_square_position[1])
        self.snake.append(new_square)