from turtle import Turtle

SCORE_COLOR = "white"
FONT = ("Times New Roman", 12, "normal")
GAME_OVER_COLOR = "red"


class ScoreBoard(Turtle):
    def __init__(self, screen, screen_height):
        super().__init__()
        self.screen = screen
        self.score = 0
        self.color(SCORE_COLOR)
        self.hideturtle()
        x = (0, round(screen_height/2)-50)
        self.penup()
        self.goto(x)
        self.display_score()

    def display_score(self):
        self.write(f"score: {self.score}", align="center", font=FONT)

    def add_score(self):
        self.score += 1
        self.clear()
        self.display_score()

    def display_game_over(self):
        self.color(GAME_OVER_COLOR)
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=FONT)
        continue_game = False
        return continue_game
