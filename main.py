from turtle import Screen
from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard
import time


screen = Screen()
screen.bgcolor("gray11")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
screen.onkey(screen.bye, "Escape")

is_game_on = True
# This is the main game
while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if (ball.distance(r_paddle) < 65 and ball.xcor() == 327 and ball.xcor() < 350) or (
            ball.distance(l_paddle) < 65 and ball.xcor() == - 327 and ball.xcor() > -351):
        ball.bounce_x()
        screen.update()
        # break

    if ball.xcor() > 380:
        score.l_point()
        ball.reset_position()
        score.update_scoreboard()
    if ball.xcor() < -380:
        score.r_point()
        ball.reset_position()
        score.update_scoreboard()

screen.exitonclick()
