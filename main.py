from ball import Ball
from turtle import Screen
from turtle import Turtle
from block import Block
import time
from scoreboard import Scoreboard

r_block = Block((350, 0))
l_block = Block((-350, 0))

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("pong")

ball = Ball()

screen.listen()
screen.onkey(r_block.up, "Up")
screen.onkey(r_block.down, "Down")
screen.onkey(l_block.up, "w")
screen.onkey(l_block.down, "s")

game_is_on = True

score = Scoreboard()
t = 0.1
while game_is_on:
    time.sleep(t)
    screen.update()
    ball.move()

    # detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_block) < 50 and ball.xcor() > 320 or ball.distance(l_block) < 50 and ball.xcor() < -320:
        if t > 0:
            t = t - 0.01
        ball.bounce_x()


    if ball.distance(r_block) > 50 and ball.xcor() > 380:

        ball.reset_position()
        score.l_point()

    if ball.distance(l_block) > 50 and ball.xcor() < -380:

        ball.reset_position()
        score.r_point()

screen.exitonclick()
