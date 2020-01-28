# MODULES, IMPORTS, LIBRARIES
import turtle
from math import pi, cos  # import single items from a library
from random import *  # imports everything locally (don't need random. in front of randrange
import random as r  # (importing twice) use your own keyboard
import import_me  # the notes document, made our own library


if __name__ == "__main__":
    # this code only runs when you run THIS FILE first
    print("Hello")
    # my_turtle = turtle.Turtle()
    print(pi)
    print(cos(0.5))
    # print(sin*0.5)
    print(randrange(1, 7))
    print(r.random())  # random float between 0 and 1
    print(import_me.x)
