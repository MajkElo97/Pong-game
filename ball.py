from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10

    def move(self):
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def collision_with_y(self):
        if self.ycor() >= 280 or self.ycor() <= -280:
            self.y_move *= -1

    def collision_with_left_paddle(self, paddle):
        if self.xcor() <= -330 and self.distance(paddle) < 50:
            self.x_move *= -1

    def collision_with_right_paddle(self, paddle):
        if self.xcor() >= 330 and self.distance(paddle) < 50:
            self.x_move *= -1
