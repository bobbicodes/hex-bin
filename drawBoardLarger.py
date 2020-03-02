import turtle
from turtle import Screen
from turtle import *

class drawBoard():
    screen = Screen()
    screen.setup(width=800, height=800, startx=10, starty=10)


    # Draw large off-white square
    turtle.hideturtle()
    turtle.speed(0)
    turtle.penup()
    turtle.goto(-350, -350)
    color('#000000', '#e4e4ff')
    begin_fill()
    turtle.pendown()
    forward(700)
    left(90)
    forward(700)
    left(90)
    forward(700)
    left(90)
    forward(700)
    end_fill()
    turtle.penup()


    #draw vertical lines
    turtle.goto(-210, 350)
    turtle.pendown()
    turtle.goto(-210, -350)
    turtle.penup()

    turtle.goto(-70, 350)
    turtle.pendown()
    turtle.goto(-70, -350)
    turtle.penup()

    turtle.goto(70, 350)
    turtle.pendown()
    turtle.goto(70, -350)
    turtle.penup()

    turtle.goto(210, 350)
    turtle.pendown()
    turtle.goto(210, -350)
    turtle.penup()

    # draw horizonal lines
    turtle.goto(-350, -210)
    turtle.pendown()
    turtle.goto(350, -210)
    turtle.penup()

    turtle.goto(-350, -70)
    turtle.pendown()
    turtle.goto(350, -70)
    turtle.penup()

    turtle.goto(-350, 70)
    turtle.pendown()
    turtle.goto(350, 70)
    turtle.penup()

    turtle.goto(-350, 210)
    turtle.pendown()
    turtle.goto(350, 210)
    turtle.penup()
    #print('Board Drawn')

