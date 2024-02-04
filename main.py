"""
create a screen
create and move  a paddle
create another paddle
create the ball and make it move
detect collision with wall and bounce
detect collision with paddle
detect collision if it misses by paddle
keep score
"""

from turtle import Screen
from ball import Ball
from paddle import Paddle
import time
from scoreboard import Score

screen = Screen()
ball = Ball()
score = Score()

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))

screen.listen()


screen.onkeypress(fun=l_paddle.up, key="w")
screen.onkeypress(fun=r_paddle.up, key="Up")
screen.onkeypress(fun=l_paddle.down, key="s")
screen.onkeypress(fun=r_paddle.down, key="Down")

screen.title("Pong game")
screen.tracer(0)
screen.bgcolor("black")
screen.setup(width=800, height=600)


game_is_on = True
while game_is_on:
    time.sleep(ball.new_speed)
    screen.update()
    ball.move()

    # detecting collision with up & down wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detecting collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # right side misses
    if ball.xcor() > 400:
        ball.start_again()
        score.l_point()

    # left side misses
    if ball.xcor() < -400:
        ball.start_again()
        score.r_point()


screen.exitonclick()

