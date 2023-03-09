from turtle import Turtle
import time

MOVE_DISTANCE = 10
SQUARE_SIZE = 20
SQUARE_COLOR = (255, 64, 64)
SNAKE_SIZE = 3


def create_one_square():
    square = Turtle(shape="square")
    square.shapesize(0.5, 0.5, 0)
    square.color(SQUARE_COLOR)
    square.penup()
    return square


def create_square_list(snake_size):
    """returns turtle square list all set to coordinate 0,0 by default"""
    list_square = []
    for _ in range(snake_size):
        square = create_one_square()
        list_square.append(square)
    return list_square


def position_snake(square_list):
    """set position for each square turtle starting with 0,0 and returns list of square"""
    x = (0, 0)
    result = []
    for square in square_list:
        x = (x[0] - SQUARE_SIZE, 0)
        square.goto(x)
        result.append(square)
    return result


class Snake:
    """List of turtle instances. User can interact with list and set its direction"""
    def __init__(self, screen, snake_speed, snake_size=SNAKE_SIZE):
        self.screen = screen
        self.screen.tracer(0)
        self.hidden_squares = []
        self.snake_size = snake_size
        self.snake_speed = snake_speed
        self.snake = create_square_list(snake_size=self.snake_size)
        self.snake = position_snake(self.snake)

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
        """move snake one square at a time depending on heading set by keypad stroke"""
        time.sleep(self.snake_speed)
        self.screen.update()
        for idx, square in enumerate(self.snake):
            current_position = square.position()
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

    def reset_snake(self):
        """hide squares after the SNAKE_SIZE one, the rest are set to their original position"""
        excess_square = self.snake[SNAKE_SIZE:]
        for square in excess_square:
            square.hideturtle()
        self.snake = self.snake[:SNAKE_SIZE]
        self.snake = position_snake(self.snake)

    def add_snake_size(self):
        """ add a square at the end of snake """
        self.snake_size += 1
        last_square_position = self.snake[-1].position()
        new_square = create_one_square()
        x = (last_square_position[0]-SQUARE_SIZE, last_square_position[1])
        new_square.goto(x)
        self.snake.append(new_square)
