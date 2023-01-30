from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.left_score = 0
        self.right_score = 0
        self.refresh_score()
        self.create_line()

    def create_line(self):
        self.goto(x=0, y=-280)
        self.setheading(90)
        while self.ycor() < 300:
            self.pendown()
            self.forward(30)
            self.penup()
            self.forward(30)

    def refresh_score(self):
        self.clear()
        self.create_line()
        self.goto(x=-50, y=260)
        self.write(self.left_score, font=('Arial', 18, 'normal'))
        self.goto(x=50, y=260)
        self.write(self.right_score, font=('Arial', 18, 'normal'))

    def add_score(self, who):
        if who == "left":
            self.left_score += 1
        else:
            self.right_score += 1
        self.refresh_score()

    def game_over(self):
        self.goto(x=0, y=0)
        self.write("GAME OVER", align="center", font=('Arial', 32, 'normal'))
