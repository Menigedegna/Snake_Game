from turtle import Screen, Turtle
from snake import Snake
from food import Food
from score_board import ScoreBoard

FONT = ("Times New Roman", 20, "normal")
MARGIN = 20
SPEED_RANGE = [0.5, 0.3, 0.1, 0.08, 0.05]
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 600
SCREEN_BG_COLOR = "black"
WINDOW_TITLE = "Snake Game"
BORDER_COLOR = "white"


def prompt_user_speed(screen_name):
    # ask user to set speed for snake
    speed = ""
    speed_range = [str(a) for a in range(len(SPEED_RANGE))]
    while speed != "None" and speed not in speed_range:
        speed = str(screen_name.textinput("Please choose a speed", "Speed is number between 0 and 4: "))
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
    turtle.pencolor(BORDER_COLOR)
    for _ in range(4):
        turtle.forward(width-2*MARGIN)
        turtle.right(90)


def start_game():
    global screen, score_max
    screen.reset()
    # ask user to set speed for snake
    speed = prompt_user_speed(screen)

    # if user doesn't click on cancel when prompted for speed => start game
    if speed != "None":
        speed = SPEED_RANGE[int(speed)]

        # draw borders for snake movement
        draw_walls(height=SCREEN_HEIGHT, width=SCREEN_WIDTH)

        # start game
        game_is_on = True
        snake = Snake(screen=screen, snake_size=3, snake_speed=speed)
        food = Food(screen=screen, screen_height=SCREEN_HEIGHT, screen_width=SCREEN_WIDTH)
        score_board = ScoreBoard(screen=screen, screen_height=SCREEN_HEIGHT)
        while game_is_on:

            # move snake
            snake.move_snake()

            # if collision with food => snake grows
            if snake.snake[0].distance(food) <= 10:
                snake.add_snake_size()
                food.move_food()
                score_board.add_score()

            # if collision with walls => game over
            x_middle = round(SCREEN_WIDTH / 2)
            y_middle = round(SCREEN_HEIGHT / 2)
            if snake.snake[0].xcor() >= x_middle - MARGIN \
                    or snake.snake[0].xcor() <= -1*x_middle + MARGIN \
                    or snake.snake[0].ycor() >= y_middle - MARGIN \
                    or snake.snake[0].ycor() <= -1*y_middle + MARGIN:
                game_is_on = score_board.display_game_over()

            # if collision with snake's tail => game over
            for square in snake.snake[1:]:
                if snake.snake[0].distance(square) <= 1:
                    game_is_on = score_board.display_game_over()

        # keep track of scores
        score_max = max(score_max, score_board.score)
        # user can restart game
        screen.listen()
        screen.onkey(key="space", fun=start_game)

    # if user click cancel when prompted for speed => close screen
    else:
        screen.bye()


if __name__ == '__main__':

    # configure screen
    screen = Screen()
    screen.bgcolor(SCREEN_BG_COLOR)
    screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    screen.title(WINDOW_TITLE)
    score_max = 0

    # start game
    start_game()

    # allow user to exit screen
    screen.exitonclick()
    print(f"Your highest score is: {score_max}")
