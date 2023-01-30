from turtle import Screen
from ball import Ball
from scoreboard import Scoreboard
from paddle import Paddle
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong arcade game")
screen.tracer(0)
screen.update()
screen.listen()

game_is_on = True

scoreboard = Scoreboard()

left_paddle = Paddle()
left_paddle.create_paddle((-350, 0))
screen.onkeypress(left_paddle.go_up, "w")
screen.onkeypress(left_paddle.go_down, "s")

right_paddle = Paddle()
right_paddle.create_paddle((350, 0))
screen.onkeypress(right_paddle.go_up, "Up")
screen.onkeypress(right_paddle.go_down, "Down")

ball = Ball()

while game_is_on:
    screen.update()
    time.sleep(0.1)
    ball.move()
    ball.collision_with_y()
    ball.collision_with_left_paddle(left_paddle)
    ball.collision_with_right_paddle(right_paddle)

    if ball.xcor() >= 380:
        scoreboard.add_score(who="left")
        ball.home()
        ball.x_move *= -1
    elif ball.xcor() <= -380:
        scoreboard.add_score(who="right")
        ball.home()
        ball.x_move *= -1

    if scoreboard.left_score >= 5 or scoreboard.right_score >= 5:
        game_is_on = False
        scoreboard.game_over()
        
screen.exitonclick()
