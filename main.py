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
    """ask user to set speed for snake and returns input"""
    speed_input = ""
    speed_range = [str(a) for a in range(len(SPEED_RANGE))]
    while speed_input != "None" and speed_input not in speed_range:
        speed_input = str(screen_name.textinput("Please choose a speed", "Speed is number between 0 and 4: "))
    return speed_input


def draw_walls(height, width):
    """draw borders around the screen"""
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
    """triggers game, user interacts with the Snake instance to catch the Food instance """
    global screen, highest_score_board, food, speed, snake, score_board
    # reset data
    food.move_food()
    score_board.reset_score()
    snake.reset_snake()
    # start game
    game_is_on = True
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
            highest_score_board.store_high_score(score_board.score)

        # if collision with snake's tail => game over
        for square in snake.snake[1:]:
            if snake.snake[0].distance(square) <= 1:
                game_is_on = score_board.display_game_over()
                highest_score_board.store_high_score(score_board.score)

    # user can restart game
    screen.listen()
    screen.onkey(key="space", fun=start_game)


if __name__ == '__main__':
    # configure screen
    screen = Screen()
    screen.bgcolor(SCREEN_BG_COLOR)
    screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    screen.title(WINDOW_TITLE)

    # ask user to set speed for snake
    speed = prompt_user_speed(screen)

    # if user doesn't click on cancel when prompted for speed => start game
    if speed != "None":
        # convert speed input into integer
        speed = SPEED_RANGE[int(speed)]

        # get recorded high score
        with open("high_score_record.txt") as file:
            data = file.read().strip()
        high_score = data.split(" = ")[1]

        # draw borders for snake movement
        draw_walls(height=SCREEN_HEIGHT, width=SCREEN_WIDTH)

        # create high score board
        highest_score_board = ScoreBoard(screen=screen, name="High score", screen_height=SCREEN_HEIGHT, x_position=80)
        highest_score_board.score = int(high_score)
        highest_score_board.clear()
        highest_score_board.display_score()

        # create game score board
        score_board = ScoreBoard(screen=screen, name="Score", screen_height=SCREEN_HEIGHT, x_position=-80)

        # create snake
        snake = Snake(screen=screen, snake_speed=speed)

        # create food
        food = Food(screen=screen, screen_height=SCREEN_HEIGHT, screen_width=SCREEN_WIDTH)

        # start game
        start_game()

        # record the highest score in txt file
        with open("high_score_record.txt", "w") as file:
            file.write(f"high_score = {highest_score_board.score}")

    # if user click cancel when prompted for speed => close screen
    else:
        screen.bye()

    # allow user to exit screen
    screen.exitonclick()
