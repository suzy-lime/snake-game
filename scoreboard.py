from turtle import Turtle
ALIGNMENT = "center"
FONT = "Arial"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.speed("fastest")
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 280)
        self.score = 0
        with open("data.txt", mode="r") as self.data:
            self.high_score = self.data.read()
        self.write(f"Score: {self.score} High Score: {self.high_score}", False, ALIGNMENT, (FONT, 12, "normal"))

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", False, ALIGNMENT, (FONT, 12, "normal"))

    def reset(self):
        with open("data.txt", mode="w") as self.data:
            if self.score > int(self.high_score):
                self.data.write(str(self.score))
        self.score = 0
        self.update_scoreboard()
