from turtle import Turtle
import time


class Snake:

    def __init__(self, screen, snake_size, snake_speed=1):
        self.screen = screen
        self.screen.tracer(0)
        self.snake_size = snake_size
        self.snake_speed = snake_speed
        self.snake = []
        x = (0, 0)
        '''create snake'''
        square_size = 20
        for _ in range(self.snake_size):
            square = Turtle(shape="square")
            square.shapesize(0.5,0.5,0)
            square.color("white")
            square.penup()
            square.goto(x)
            x = (x[0]-square_size, 0)
            self.snake.append(square)

    def move_left(self):
        self.snake[0].left(40)

    def move_right(self):
        self.snake[0].right(40)

    def move_snake(self):
        time.sleep(self.snake_speed/10)
        self.screen.update()
        '''move snake one square at a time'''
        for idx, square in enumerate(self.snake):
            current_position = square.position()
            # square.speed(snake_speed)
            if idx == 0:
                square.forward(10)
            else:
                square.goto(previous_position)
            previous_position = current_position
        self.screen.listen()
        self.screen.onkey(key="a", fun=self.move_left)
        self.screen.onkey(key="d", fun=self.move_right)


