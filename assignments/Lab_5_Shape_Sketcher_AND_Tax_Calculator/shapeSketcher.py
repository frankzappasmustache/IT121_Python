"""
    Project Name: IT121_Python
    Sub-project: Labs
    File Name: shapeSketcher.py
    Author: Dustin McClure
    Lab: Lab 5a - Shape Sketcher
    Modified Date: 11/05/2020

    Python Shape Sketcher Program
"""
import turtle
from turtle import Turtle, Screen

t = turtle.Pen()
screen = turtle.Screen()
t.speed(10)
t.pensize(4)
screen.title("Sketchy Shapes")

pen_fill_colors = {0: '#fb4934', 1: '#b8bb26', 2: '#fabd2f', 3: '#83a598', 4: '#d3869b', 5: '#8ec07c', 6: '#fe8019', 7: '#cc241d', 8: '#98971a', 9: '#d79921', 10: '#458588', 11: '#b16286', 12: '#689d6a', 13: '#d65d0e', 14: '#9d0006', 15: '#79740e', 16: '#b57614', 17: '#076678', 18: '#8f3f71', 19: '#427b58', 20: '#af3a03'}

bg_colors = {0: '#1d2021', 1: '#282828', 2: '#32302f', 3: '#3c3836', 4: '#504945', 5: '#665c54', 6: '#7c6f64', 7: '#928374', 8: '#f9f5d7', 9: '#fbf1c7', 10: '#f2e5bc', 11: '#ebdbb2', 12: '#d5c4a1', 13: '#bdae93', 14: '#a89984'}

PROMPT = '''
                      1: Rectangle
                      2: Circle
                      3: Triangle
                      4: Hexagon
                      5: EXIT PROGRAM'''
PROMPT1 = '''
                      0: red_orange
                      1: key_lime_pie
                      2: lightning_yellow
                      3: sea_nymph
                      4: can_can
                      5: olivine
                      6: pumpkin
                      7: thunderbird
                      8: hacienda
                      9: golden_grass
                      10: faded_jade
                      11: tapestry
                      12: highland
                      13: christine
                      14: sangria
                      15: spicy_mustard
                      16: reno_sand
                      17: atoll
                      18: cannon_pink
                      19: goblin
                      20: fire
                      '''
PROMPT2 = '''
                      0: shark
                      1: mine_shaft
                      2: dune
                      3: dune_lighter
                      4: masala
                      5: pine_cone
                      6: sandstone
                      7: stonewall
                      8: citrine_white
                      9:  double_pearl_lusta
                      10: sidecar
                      11: chamois
                      12: akaroa
                      13: indian_khaki
                      14: donkey_brown
                      '''
def select_colors():

    pen_color = screen.numinput("Color for shape borders:", prompt=PROMPT1)

    color = int(pen_color)
    final_pen = pen_fill_colors[color]

    fill_color = screen.numinput("Color for shape fill:", prompt=PROMPT1)

    fill = int(fill_color)
    final_fill = pen_fill_colors[fill]

    bg_color = screen.numinput("Screen background color:", prompt=PROMPT2)

    bg = int(bg_color)
    final_bg = bg_colors[bg]
    return [final_pen, final_fill, final_bg]

def rect(t, size1, size2, final_pen, final_fill, final_bg, angle=90):
    t.reset()
    pass
    screen.bgcolor(final_bg)
    t.color(final_pen, final_fill)
    t.begin_fill()
    t.forward(size1)
    t.left(angle)
    t.forward(size2)
    t.left(angle)
    t.forward(size1)
    t.left(angle)
    t.forward(size2)
    t.end_fill()


def circle(t, size1, final_pen, final_fill, final_bg):
    t.reset()
    pass
    screen.bgcolor(final_bg)
    t.color(final_pen, final_fill)
    t.begin_fill()
    t.circle(size1)
    t.end_fill()


def triangle(t, size1, final_pen, final_fill, final_bg, angle=120):
    t.reset()
    pass
    screen.bgcolor(final_bg)
    t.color(final_pen, final_fill)
    t.begin_fill()
    t.forward(size1)
    t.left(angle)
    t.forward(size1)
    t.left(angle)
    t.forward(size1)
    t.end_fill()


def hexagon(t, size1, final_pen, final_fill, final_bg, angle=60):
    t.reset()
    pass
    screen.bgcolor(final_bg)
    t.color(final_pen, final_fill)
    for x in range(1, 7):
        t.begin_fill()
        t.forward(size1)
        t.right(angle)
        t.end_fill()

def draw_shape():
    while True:
        COMMANDS = [rect, circle, triangle, hexagon, quit]

        selection = screen.numinput("Select a shape you sketchy individual!",
           prompt=PROMPT)
        shape = int(selection)

        if shape == 0:
            size1 = input('''
              Please enter a size for the first two sides of your rectangle;\n
              valid options are any number between 50 and 100:
              ''')
            size2 = input('''
              Please enter a size for the second two sides of your rectangle;\n
              valid options are any number between 50 and 100:
              ''')
            COMMANDS[shape](t, size1, size2, final_pen=final_pen,
              final_fill=final_fill, final_bg=final_bg, angle=90)
        elif shape == 1:
            size1 = input('''
            Please enter a size you would like to make your circle;\n
            valid options are any number between 50 and 100:
            ''')
            COMMANDS[shape]()
        elif shape == 2:
          size1 = input('''
            Please enter a size for the sides of your triangle;\n
             valid options are any number between 50 and 100:
             ''')
          COMMANDS[shape]()
        elif shape == 3:
          size1 = input('''
            Please enter a size for the sides of your hexagon;\n
            valid options are any number between 50 and 100:
            ''')
          COMMANDS[shape]()
        elif shape == 4:
          exit()

print("===========================================\n")
print("Welcome to sketchy shapes!\n")
print("===========================================\n")

select_colors()
draw_shape()
