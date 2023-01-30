from turtle import Turtle


class Paddle(Turtle):

    def __init__(self):
        super().__init__()

    def create_paddle(self, position):
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)

    def go_up(self):
        if self.ycor() < 250:
            new_y = self.ycor() + 20
            self.goto(self.xcor(), y=new_y)

    def go_down(self):
        if self.ycor() > -250:
            new_y = self.ycor() - 20
            self.goto(self.xcor(), y=new_y)
