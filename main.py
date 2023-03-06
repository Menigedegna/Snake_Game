from turtle import Screen, Turtle
from snake import Snake
from food import Food
from score_board import ScoreBoard

FONT = ("Times New Roman", 20, "normal")
MARGIN = 20


def prompt_user_speed(screen_name):
    # ask user to set speed for snake
    speed = ""
    while speed == "" or speed not in list(range(5)):
        speed = int(screen_name.textinput("Please choose a speed", "Speed is number between 0 and 4: "))
    return speed


def draw_walls(height, width):
    turtle = Turtle()
    turtle.hideturtle()
    turtle.penup()
    x = (-1*round(width/2)+MARGIN, round(height/2)-MARGIN)
    turtle.speed("fastest")
    turtle.goto(x)
    turtle.pendown()
    turtle.pensize(6)
    turtle.pencolor("white")
    for _ in range(4):
        turtle.forward(width-2*MARGIN)
        turtle.right(90)


def start_game():
    global screen, score_max
    screen.reset()
    speed = prompt_user_speed(screen)
    draw_walls(height=screen_height, width=screen_width)
    # start game
    game_is_on = True
    snake = Snake(screen=screen, snake_size=3, snake_speed=speed)
    food = Food(screen=screen, screen_height=screen_height, screen_width=screen_width)
    score_board = ScoreBoard(screen=screen, screen_height=screen_height)
    while game_is_on:

        # move snake
        snake.move_snake()

        # detect collision with food
        if snake.snake[0].distance(food) <= 10:
            snake.add_snake_size()
            food.move_food()
            score_board.add_score()

        # detect collision with walls
        if snake.snake[0].xcor() >= round(screen_width / 2)-MARGIN \
                or snake.snake[0].xcor() <= -1*round(screen_width / 2)+MARGIN \
                or snake.snake[0].ycor() >= round(screen_height / 2)-MARGIN \
                or snake.snake[0].ycor() <= -1*round(screen_height / 2)+MARGIN:
            game_is_on = score_board.display_game_over()

        # detect collision with snake's tail
        if snake.snake[0].distance(snake.snake[-1]) <= 2:
            game_is_on = score_board.display_game_over()

    # keep track of scores
    score_max = max(score_max, score_board.score)
    # restart game
    screen.listen()
    screen.onkey(key="space", fun=start_game)


if __name__ == '__main__':

    # configure screen
    screen = Screen()
    screen.bgcolor("black")
    screen_width = 600
    screen_height = 600
    screen.setup(width=screen_width, height=screen_height)
    screen.title("Snake Game")
    score_max = 0
    start_game()

    # allow user to exit screen
    screen.exitonclick()
    print(f"Your highest score is: {score_max}")
