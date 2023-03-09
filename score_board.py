from turtle import Turtle

SCORE_COLOR = (30, 144, 255)
SCORE_FONT = ("Times New Roman", 12, "normal")
ALERT_FONT = ("Times New Roman", 18, "normal")

GAME_OVER_COLOR = (255, 64, 64)


class ScoreBoard(Turtle):
    """Turtle  displays score and game status on screen"""
    def __init__(self, name, screen, screen_height, x_position):
        super().__init__()
        self.screen = screen
        self.screen_height = screen_height
        self.x_position = x_position
        self.score = 0
        self.name = name
        self.color(SCORE_COLOR)
        self.hideturtle()
        self.reset_score_position()
        self.display_score()

    def reset_score_position(self):
        x = (self.x_position, round(self.screen_height/2)-50)
        self.penup()
        self.goto(x)

    def display_score(self):
        """display score on screen"""
        self.color(SCORE_COLOR)
        self.write(f"{self.name}: {self.score}", align="center", font=SCORE_FONT)

    def add_score(self):
        """increment score and displays it on screen"""
        self.score += 1
        self.clear()
        self.display_score()

    def display_game_over(self):
        self.color(GAME_OVER_COLOR)
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=ALERT_FONT)
        continue_game = False
        return continue_game

    def store_high_score(self, round_score):
        """determines the highest score recorded after each round of game while screen is closed"""
        self.score = max(self.score, round_score)
        self.clear()
        self.display_score()

    def reset_score(self):
        """reset score and display position"""
        self.score = 0
        self.clear()
        self.reset_score_position()
        self.display_score()
