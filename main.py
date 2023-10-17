from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.title('Pong Game')
screen.bgcolor('black')

# pause the animation
screen.tracer(0)

r_paddle = Paddle(350)
l_paddle = Paddle(-350)

ball = Ball()
scoreboard = ScoreBoard()

# listen for key strikes
screen.listen()
screen.onkeypress(r_paddle.move_up, 'Up')
screen.onkeypress(r_paddle.move_down, 'Down')
screen.onkeypress(l_paddle.move_up, 'w')
screen.onkeypress(l_paddle.move_down, 's')

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    # starts the animation again
    screen.update()
    ball.move()

    # detect collision with walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # detect miss R paddle
    if ball.xcor() > 380:

        ball.reset_position()
        scoreboard.l_point()

    # detect miss L paddle
    if ball.xcor() < -380:

        ball.reset_position()
        scoreboard.r_point()



screen.exitonclick()
