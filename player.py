from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self, shape="turtle"):
        super().__init__(shape)
        self.penup()
        self.color("black")
        self.setheading(90)
        self.start_position()

    def start_position(self):
        self.goto(STARTING_POSITION)

    def turtle_run(self):
        self.forward(MOVE_DISTANCE)

    def cross_finish(self):
        if self.ycor() > FINISH_LINE_Y:
            self.start_position()
            return True
