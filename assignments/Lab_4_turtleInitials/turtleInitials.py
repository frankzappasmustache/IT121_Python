"""
    Project Name: IT121_Python
    Sub-project: Labs
    File Name: tt.py
    Author: Dustin McClure
    Lab: Lab 4 - t
    Modified Date: 10/23/2020

    Just drawing my initials with *queue Dana Carvey* turtle.
"""
import turtle
from turtle import Turtle, Screen

NAME = "DTM"

t = turtle.Pen()

BORDER = 2
BOX_WIDTH, BOX_HEIGHT =3, 5  # letter bounding box
WIDTH, HEIGHT = BOX_WIDTH - BORDER * 2, BOX_HEIGHT - BORDER * 2  # letter size

def draw_D(t):
    t.forward(HEIGHT)
    t.right(90)
    t.circle(-HEIGHT / 2, 180, 30)

def draw_T(t):
    t.forward(HEIGHT)
    t.left(90)
    t.forward(WIDTH / 2)
    t.backward(WIDTH)

def draw_M(t):
    t.forward(HEIGHT)
    t.right(340)
    t.backward(HEIGHT / 2)
    t.right(60)
    t.forward(HEIGHT / 2)
    t.left(120)
    t.backward(HEIGHT)

LETTERS = {'D': draw_D,'T': draw_T, 'M': draw_M}

wn = Screen()
wn.setup(1920, 1080)
wn.title("Turtle writing my name: {}".format(NAME))
wn.setworldcoordinates(0, 0, BOX_WIDTH * len(NAME), BOX_HEIGHT)

marker = Turtle()

for counter, letter in enumerate(NAME):
    marker.penup()
    marker.goto(counter * BOX_WIDTH + BORDER, BORDER)
    marker.setheading(90)

    if letter in LETTERS:
        marker.pendown()
        LETTERS[letter](marker)

marker.hideturtle()

wn.mainloop()
