"""
    Project Name: IT121_Python
    Sub-project: Labs
    File Name: shapeSketcher.py
    Author: Dustin McClure
    Lab: Lab 5a - Shape Sketcher
    Modified Date: 11/09/2020

    Python Shape Sketcher Program
"""
# import turtle, and from turtle Turtle and Screen
import turtle
from turtle import Turtle, Screen

# create a new instance of turtle.Pen() - t, new instance of
# turtle.Screen() - screen
t = turtle.Pen()
screen = turtle.Screen()

# set mode to logo, speed to 4, and pensize to 4
turtle.mode('logo')
t.speed(5)
t.pensize(4)

# set screensize to that of full HD monitor, and set turlte window title
turtle.screensize(canvwidth=1920, canvheight=1080)
screen.title("SKETCHY SHAPES: A Shape Maker for Sketchy People")

# define dict of colors to be used for pen color and fill color
# you will notice if you look at the pen, fill, and bg colors, they are based
# on my editor's color scheme - Gruvbox'
pen_fill_colors = {0: '#fb4934', 1: '#b8bb26', 2: '#fabd2f', 3: '#83a598', 4: '#d3869b', 5: '#8ec07c', 6: '#fe8019', 7: '#cc241d', 8: '#98971a', 9: '#d79921', 10: '#458588', 11: '#b16286', 12: '#689d6a', 13: '#d65d0e', 14: '#9d0006', 15: '#79740e', 16: '#b57614', 17: '#076678', 18: '#8f3f71', 19: '#427b58', 20: '#af3a03'}

# define dict of colors to be used as background colors
bg_colors = {0: '#1d2021', 1: '#282828', 2: '#32302f', 3: '#3c3836', 4: '#504945', 5: '#665c54', 6: '#7c6f64', 7: '#928374', 8: '#f9f5d7', 9: '#fbf1c7', 10: '#f2e5bc', 11: '#ebdbb2', 12: '#d5c4a1', 13: '#bdae93', 14: '#a89984'}

# define dict of sizes for shape sides so user can choose to draw shapes of different sizes
sizes = {0: 100, 1: 200, 2: 300, 3: 400, 4: 500}

# create numbered text list as prompt that has options for all shape defs,
# and an option to exit the program
PROMPT = "0. Rectangle\n1. Circle\n2. Triangle\n3. Hexagon\n4. EXIT PROGRAM"

# create numbered text prompt that has options for all of the colors
# stored in the pen_fill_colors dict. You will notice the number corresponds
# to each dict value's key
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

# create numbered text prompt that has options for all of the colors
# stored in the bg_colors dict. You will notice the number corresponds
# to each dict value's key
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

# create numbered text prompt that has options for all of the different shape
# sizes available in the sizes dict with each number corresponding to it's
# dict key
PROMPT3 = '''
        0. 100
        1. 200
        2. 300
        3. 400
        4. 500
        '''

# function def to select shape pen color, fill color, and bg_color of screen
def select_colors():

    # for each color, request user input in the form of an integer, using
    # prompt1 as the selection list, store the corresponding color in the
    # final_* variable by equating it to the correct index value for each
    # dict's key
    pen_color = int(screen.numinput("Shape Border Color:", prompt=PROMPT1))
    final_pen = pen_fill_colors[pen_color]

    fill_color = int(screen.numinput("Shape Fill Color:", prompt=PROMPT1))
    final_fill = pen_fill_colors[fill_color]

    bg_color = int(screen.numinput("Screen Background Color:", prompt=PROMPT2))
    final_bg = bg_colors[bg_color]

    # return the variables with their newly assigned color code values
    return final_pen, final_fill, final_bg

# function def for a rectangle, taking 2 side length args, color args, and
# the pre-defined var angle
def rect(size1, size2, final_pen, final_fill, final_bg, angle = 90):

    # set screen bgcolor/pencolor/fillcolor, instruct turtle to begin fill,
    # make appropriate movements on canvas based on the users size input and
    # pre-defined angle, and then instruct turtle to end color fill
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

# function def for a circle, taking 1 size arg for the radius, and color args
def circle(size1, final_pen, final_fill, final_bg):

    # set screen bgcolor/pencolor/fillcolor, instruct turtle to begin fill,
    # make appropriate movements on canvas based on the users size input
    # and then instruct turtle to end color fill
    screen.bgcolor(final_bg)
    t.pencolor(final_pen)
    t.fillcolor(final_fill)
    t.begin_fill()
    t.circle(size1)
    t.end_fill()

# function def for an equilateral triangle, taking 1 side length arg, color
# args, and the pre-defined var angle
def triangle(size1, final_pen, final_fill, final_bg, angle = 120):

    # set screen bgcolor/pencolor/fillcolor, instruct turtle to begin fill,
    # make appropriate movements on canvas based on the users size input and
    # pre-defined angle, and then instruct turtle to end color fill
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

# function def for a hexagon, taking 1 side length arg, color
# args, and the pre-defined var angle
def hexagon(size1, final_pen, final_fill, final_bg, angle = 60):

    # set screen bgcolor/pencolor/fillcolor
    screen.bgcolor(final_bg)
    t.pencolor(final_pen)
    t.fillcolor(final_fill)

    # in for loop, for x (each side), in range 1 - 7
    # (6 sides will be drawn ** 7 does not get included in the range):
    # insturct turtle to begin fill, draw a side of the size in size1, turn
    # at an angle dfined by the angle var, and then stop filling
    for x in range(1, 7):
        t.begin_fill()
        t.forward(size1)
        t.right(angle)
        t.end_fill()

# when the user wants to quit, use the built in turlte.bye() function to
# close the canvas window
def quit():
    turtle.bye()

# function def to draw shapes
def draw_shape():

    # define index of commands that correspond to the different function
    # defs for our shapes, and the function def to quit the program
    COMMANDS = [rect, circle, triangle, hexagon, quit]

    # use a while true loop to loop for an indefinite amount of time until user
    # calls option number 4 to quit the program
    while True:

        # prompt the user for input to select a shape (stored as int) or exit.
        # Each selection corresponds with it's position in the commands index
        # and is checked in the following if/elif loop
        shape = int(screen.numinput("Select a shape you sketchy individual!",
            prompt=PROMPT))

        # after a selection is made, clear the canvas if there is anything
        # on it
        t.clear()

        # use if/elif loop to check if the shape var == int, if so, do code
        # tkinter will throw an error if an invalid selection is made, and
        # return user to prompt
        if shape == 0:

            # unpack and assign return values from select colors() function
            final_pen, final_fill, final_bg = select_colors()

            # get user input (as int) for size of rect sides, store ints in
            # SizeOne and SizeTwo vars
            sizeOne = int(screen.numinput('''
              Please enter a size for the first two sides of your rectangle;\n
              valid options are any number between 50 and 100:
              ''', prompt = PROMPT3))
            sizeTwo = int(screen.numinput('''
              Please enter a size for the second two sides of your rectangle;\n
              valid options are any number between 50 and 100:
              ''', prompt = PROMPT3))

            # look up the corresponding key, and in sizes dict storing it in
            # size1 and size2
            size1 = sizes[sizeOne]
            size2 = sizes[sizeTwo]

            # call the command corresponding to the int stored in shape var by
            # looking up it's index in COMMANDS. Fill in all required
            # arg vars for the shape
            COMMANDS[shape](size1, size2, final_pen, final_fill, final_bg)

            # continue to beginning of while loop to start again
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
            # if shape index is equat to the quit function exit the program
            COMMANDS[shape]()

# call function
draw_shape()
