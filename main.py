from turtle import Screen
from snake import Snake
from food import Food


if __name__ == '__main__':
    screen = Screen()
    screen.bgcolor("black")
    screen_width = 800
    screen_height = 800
    screen.setup(width=screen_width, height=screen_height)
    screen.title("Snake Game")

    game_is_on = True
    snake = Snake(screen=screen, snake_size=3, snake_speed=1)
    food = Food(screen=screen, screen_height=screen_height, screen_width=screen_width)
    snake_ate_food = False
    while game_is_on:
        if snake.snake[0].distance(food) <= 10:
            print("got it")
            snake.add_snake_size()
            food.move_food()
        snake.move_snake()

    # allow user to exit screen
    screen.exitonclick()
