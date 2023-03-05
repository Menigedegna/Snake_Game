from turtle import Turtle, Screen
import time

class Snake:

    def __init__(self):
        self.screen = Screen()
        self. screen.bgcolor("black")
        self.screen.setup(width=800, height=800)
        self.screen.title("Snake Game")
        self.screen.tracer(0)
        self.snake = []
        self.game_is_on = True

    def create_snake(self, snake_size):
        x = (0, 0)
        square_size = 20
        for _ in range(snake_size):
            square = Turtle(shape="square")
            square.color("white")
            square.penup()
            square.goto(x)
            x = (x[0]-square_size, 0)
            self.snake.append(square)

    def move_snake(self, snake_size, snake_speed):
        self.create_snake(snake_size)
        while self.game_is_on:
            time.sleep(snake_speed/10)
            self.screen.update()
            for idx, square in enumerate(self.snake):
                current_position = square.position()
                # square.speed(snake_speed)
                if idx == 0:
                    square.forward(20)
                else:
                    square.goto(previous_position)
                previous_position = current_position
