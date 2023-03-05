from turtle import Screen
from snake import Snake


if __name__ == '__main__':
    screen = Screen()
    screen.bgcolor("black")
    screen.setup(width=800, height=800)
    screen.title("Snake Game")

    game_is_on = True
    snake = Snake(screen=screen, snake_size=3, snake_speed=1)
    while game_is_on:
        snake.move_snake()
    # allow user to exit screen
    screen.exitonclick()