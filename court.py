from turtle import Turtle


class Court(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=0.1)
        self.penup()
        self.goto(position)
