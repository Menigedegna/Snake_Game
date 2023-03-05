from snake import Snake


if __name__ == '__main__':
    snake = Snake()
    snake.move_snake(snake_size=3, snake_speed=1)
    # allow user to exit screen
    snake.screen.exitonclick()