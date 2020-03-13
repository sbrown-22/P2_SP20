
# Turtle Recursion (30pts)

# 1)  Using the turtle library, create the H fractal pattern as shown in the image (htree4.jpg) in this directory. (15pts)

import turtle

my_turtle = turtle.Turtle()
my_turtle.shape("turtle")
my_turtle.speed(0)

my_screen = turtle.Screen()
my_screen.bgcolor('white')


my_turtle.home()


def h_letter(x, y, width, height, depth):

    if depth > 0:
        my_turtle.width(4)
        my_turtle.up()
        my_turtle.goto(x, y)
        my_turtle.down()

        my_turtle.goto(x, y + height / 2)
        my_turtle.down()
        my_turtle.goto(x, y - height / 2)

        my_turtle.up()
        my_turtle.goto(x, y)
        my_turtle.down()
        my_turtle.goto(x + width, y)

        my_turtle.up()
        my_turtle.goto(x + width, y + height / 2)
        my_turtle.down()
        my_turtle.goto(x + width, y - height / 2)

        h_letter(x - width / 4, y + height / 2, width / 2, height / 2, depth - 1)
        h_letter(x - width / 4, y - height / 2, width / 2, height / 2, depth - 1)
        h_letter(x + 3 * width / 4, y + height / 2, width / 2, height / 2, depth - 1)
        h_letter(x + 3 * width / 4, y - height / 2, width / 2, height / 2, depth - 1)


h_letter(-150, 0, 300, 300, 4)
my_screen.clear()


# 2)  Using the turtle library, create any of the other recursive patterns in the directory. (10pts)

my_turtle.home()

def plus_fractal(x, y, width, height, depth):

    my_turtle.width(2)
    my_turtle.up()
    my_turtle.goto(x, y)

    if depth > 0:
        my_turtle.width(2)
        my_turtle.up()
        my_turtle.goto(x, y)

        my_turtle.down()
        my_turtle.goto(x + width / 2, y)
        my_turtle.goto(x, y)
        my_turtle.goto(x - width / 2, y)
        my_turtle.goto(x, y)
        my_turtle.goto(x, y + height / 2)
        my_turtle.goto(x, y)
        my_turtle.goto(x, y - height / 2)

        plus_fractal(x + width / 2, y, width / 2, height / 2, depth - 1)
        plus_fractal(x - width / 2, y, width / 2, height / 2, depth - 1)
        plus_fractal(x, y + height / 2, width / 2, height / 2, depth - 1)
        plus_fractal(x, y - height / 2, width / 2, height / 2, depth - 1)


plus_fractal(0, 0, 300, 300, 4)
my_screen.clear()

# 3)  Create your own work of art with a repeating pattern of your making.
# It must be a repeated pattern using recursion. Snowflakes, trees, and spirals are a common choice.
# Or you can create a third one from the directory. (5pt)

# Each fractal should
# - be recursive
# - have a depth of at least 4
# - be contained on the screen
# Have fun!

my_turtle.home()
import random


def morse_code_pattern(x, y, width, height, depth):
    if depth > 0:
        colors = ['black', 'white']
        color = random.choice(colors)
        my_turtle.width(4)
        my_turtle.up()

        my_turtle.fillcolor(color)
        my_turtle.begin_fill()

        my_turtle.goto(x, y)
        my_turtle.down()
        my_turtle.goto(x + 11, y)
        my_turtle.down()
        my_turtle.goto(x + 11, y - 11)
        my_turtle.down()
        my_turtle.goto(x, y - 11)
        my_turtle.down()
        my_turtle.goto(x, y)

        my_turtle.end_fill()

        morse_code_pattern(x + width, y, width, height, depth - 1)
        morse_code_pattern(-356, y - height, width, height, 64)


morse_code_pattern(-356, 335, 11, 11, 64)

