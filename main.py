from turtle import Screen
import random
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard, InfoArea
from bricks import BricksWall
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=1800, height=900)
screen.title("Breakout Game")
screen.tracer(0)

player = Paddle((0, -370))
ball = Ball()
info_area = InfoArea()
scoreboard = Scoreboard()
wall = BricksWall()
speed = 0.1

screen.listen()

screen.onkeypress(fun=player.move_left, key="Left")
screen.onkeypress(fun=player.move_right, key="Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)

    ball.move()
    player.color("DeepSkyBlue")

    # Detect collision with bricks
    for brick in wall.bricks:
        if (ball.xcor() in range(brick.xcor()-50,brick.xcor()+50)) and (ball.ycor() in range(brick.ycor()-50, brick.ycor()+50)):
            wall.remove_brick(brick)
            brick.reset()
            ball.bounce_y()
            scoreboard.score_update(10)

    # Level up
    if len(wall.bricks) == 0:
        scoreboard.level_up()
        wall.reset()
        ball.reset_position(player.xcor())


    # Detect collision with top wall
    if ball.ycor() > 388:
        ball.bounce_y()

    # Detect collision with lateral walls
    if ball.xcor() < -888 or ball.xcor() > 888:
        ball.bounce_x()

    # Detect collision with paddles
    if (ball.xcor() in range(player.xcor()-150,player.xcor()+150)) and (ball.ycor() < -350):
        player.color("DarkBlue")
        ball.bounce_y()
        ball.increase_speed(speed_factor=0.95)
        scoreboard.speed_update(speed=ball.move_speed)


    #  Paddle misses
    if ball.ycor() < -380:
        scoreboard.decrease_life()
        ball.reset_position(player.xcor())
        scoreboard.speed_update(speed=ball.move_speed)


    # Game over
    if scoreboard.end_game:
        ball.goto(player.xcor(),-355)
        player.color("DarkBlue")
        print("Game over")
        screen.onkeypress(fun=scoreboard.reset_score, key="space")




screen.exitonclick()