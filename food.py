from turtle import Turtle
from random import randint

MARGIN = 40
FOOD_COLOR = "yellow"


class Food(Turtle):
    """Turtle pops randomly on screen at the beginning of each game round"""
    def __init__(self, screen, screen_height, screen_width):
        super().__init__()
        self.screen = screen
        self.shape("circle")
        self.shapesize(0.3, 0.3, 0)
        self.color(FOOD_COLOR)
        self.penup()
        self.screen_width_center = round(screen_width/2) - MARGIN
        self.screen_height_center = round(screen_height/2) - MARGIN

    def move_food(self):
        """position food instance"""
        xcor = randint(-1*self.screen_width_center, self.screen_width_center)
        ycor = randint(-1*self.screen_height_center, self.screen_height_center)
        self.goto(xcor, ycor)
