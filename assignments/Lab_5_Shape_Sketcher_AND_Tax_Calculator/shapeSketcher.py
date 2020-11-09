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
turtle.mode('logo')
t.speed(5)
t.pensize(4)
turtle.screensize(canvwidth=1920, canvheight=1080)
screen.title("SKETCHY SHAPES: A Shape Maker for Sketchy People")

pen_fill_colors = {0: '#fb4934', 1: '#b8bb26', 2: '#fabd2f', 3: '#83a598', 4: '#d3869b', 5: '#8ec07c', 6: '#fe8019', 7: '#cc241d', 8: '#98971a', 9: '#d79921', 10: '#458588', 11: '#b16286', 12: '#689d6a', 13: '#d65d0e', 14: '#9d0006', 15: '#79740e', 16: '#b57614', 17: '#076678', 18: '#8f3f71', 19: '#427b58', 20: '#af3a03'}

bg_colors = {0: '#1d2021', 1: '#282828', 2: '#32302f', 3: '#3c3836', 4: '#504945', 5: '#665c54', 6: '#7c6f64', 7: '#928374', 8: '#f9f5d7', 9: '#fbf1c7', 10: '#f2e5bc', 11: '#ebdbb2', 12: '#d5c4a1', 13: '#bdae93', 14: '#a89984'}
sizes = {0: 100, 1: 200, 2: 300, 3: 400, 4: 500}

PROMPT = "0. Rectangle\n1. Circle\n2. Triangle\n3. Hexagon\n4. EXIT PROGRAM"
PROMPT1 = '''
        0. red_orange
        1. key_lime_pie
        2. lightning_yellow
        3. sea_nymph
        4. can_can
        5. olivine
        6. pumpkin
        7. thunderbird
        8. hacienda
        9. golden_grass
        10. faded_jade
        11. tapestry
        12. highland
        13. christine
        14. sangria
        15. spicy_mustard
        16. reno_sand
        17. atoll
        18. cannon_pink
        19. goblin
        20. fire
                      '''
PROMPT2 = '''
        0. shark
        1. mine_shaft
        2. dune
        3. dune_lighter
        4. masala
        5. pine_cone
        6. sandstone
        7. stonewall
        8. citrine_white
        9.  double_pearl_lusta
        10. sidecar
        11. chamois
        12. akaroa
        13. indian_khaki
        14. donkey_brown
                      '''
PROMPT3 = '''
        0. 100
        1. 200
        2. 300
        3. 400
        4. 500
        '''

def select_colors():

    pen_color = int(screen.numinput("Shape Border Color:", prompt=PROMPT1))
    final_pen = pen_fill_colors[pen_color]

    fill_color = int(screen.numinput("Shape Fill Color:", prompt=PROMPT1))
    final_fill = pen_fill_colors[fill_color]

    bg_color = int(screen.numinput("Screen Background Color:", prompt=PROMPT2))
    final_bg = bg_colors[bg_color]

    return final_pen, final_fill, final_bg

def rect(size1, size2, final_pen, final_fill, final_bg, angle = 90):
    screen.bgcolor(final_bg)
    t.pencolor(final_pen)
    t.fillcolor(final_fill)
    t.begin_fill()
    t.forward(size1)
    t.left(angle)
    t.forward(size2)
    t.left(angle)
    t.forward(size1)
    t.left(angle)
    t.forward(size2)
    t.end_fill()


def circle(size1, final_pen, final_fill, final_bg):
    screen.bgcolor(final_bg)
    t.pencolor(final_pen)
    t.fillcolor(final_fill)
    t.begin_fill()
    t.circle(size1)
    t.end_fill()


def triangle(size1, final_pen, final_fill, final_bg, angle = 120):
    screen.bgcolor(final_bg)
    t.pencolor(final_pen)
    t.fillcolor(final_fill)
    t.begin_fill()
    t.forward(size1)
    t.left(angle)
    t.forward(size1)
    t.left(angle)
    t.forward(size1)
    t.end_fill()


def hexagon(size1, final_pen, final_fill, final_bg, angle = 60):
    screen.bgcolor(final_bg)
    t.pencolor(final_pen)
    t.fillcolor(final_fill)
    for x in range(1, 7):
        t.begin_fill()
        t.forward(size1)
        t.right(angle)
        t.end_fill()

def quit():
    turtle.bye()

def draw_shape():
    COMMANDS = [rect, circle, triangle, hexagon, quit]
    while True:
        shape = int(screen.numinput("Select a shape you sketchy individual!",
            prompt=PROMPT))
        t.clear()

        if shape == 0:
            final_pen, final_fill, final_bg = select_colors()
            sizeOne = int(screen.numinput('''
              Please enter a size for the first two sides of your rectangle;\n
              valid options are any number between 50 and 100:
              ''', prompt = PROMPT3))
            sizeTwo = int(screen.numinput('''
              Please enter a size for the second two sides of your rectangle;\n
              valid options are any number between 50 and 100:
              ''', prompt = PROMPT3))
            size1 = sizes[sizeOne]
            size2 = sizes[sizeTwo]
            COMMANDS[shape](size1, size2, final_pen, final_fill, final_bg)
            continue
        elif shape == 1:
            final_pen, final_fill, final_bg = select_colors()
            sizeOne = int(screen.numinput('''
              Please enter a size for the first two sides of your rectangle;\n
              valid options are any number between 50 and 100:
              ''', prompt = PROMPT3))
            size1 = sizes[sizeOne]
            COMMANDS[shape](size1, final_pen, final_fill, final_bg)
            continue
        elif shape == 2:
            final_pen, final_fill, final_bg = select_colors()
            sizeOne = int(screen.numinput('''
              Please enter a size for the first two sides of your rectangle;\n
              valid options are any number between 50 and 100:
              ''', prompt = PROMPT3))
            size1 = sizes[sizeOne]
            COMMANDS[shape](size1, final_pen, final_fill, final_bg)
            continue
        elif shape == 3:
            final_pen, final_fill, final_bg = select_colors()
            sizeOne = int(screen.numinput('''
              Please enter a size for the first two sides of your rectangle;\n
              valid options are any number between 50 and 100:
              ''', prompt = PROMPT3))
            size1 = sizes[sizeOne]
            COMMANDS[shape](size1, final_pen, final_fill, final_bg)
            continue
        elif shape == 4:
            COMMANDS[shape]()

draw_shape()
