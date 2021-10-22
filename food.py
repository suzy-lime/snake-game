from turtle import Turtle
import random

COLORS = ["LightBlue", "LightPink", "LightSalmon3", "IndianRed1", "plum1", "LightSkyBlue", "PaleTurquoise2",
          "PaleVioletRed1", "PowderBlue", "MediumSeaGreen", "wheat2", "SeaGreen4", "SlateGrey"]


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")
        self.color_refresh()
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)

    def color_refresh(self):
        random_color = random.choice(COLORS)
        self.color(random_color)
