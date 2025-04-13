from turtle import Turtle

FONT = ("Courier", 24, "normal")


class ScoreBoard(Turtle):

    def __init__(self, y_position):
        super().__init__()

        self.hideturtle()
        self.penup()
        self.goto(0, y_position)
        self.score = 0
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"Level: {self.score}", font=FONT, align="center")

    def new_level(self):
        self.score += 1
        self.write_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", font=FONT, align="center")
