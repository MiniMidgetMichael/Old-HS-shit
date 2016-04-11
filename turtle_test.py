#! C:UsersMichaelLFarwellAppDataLocalProgramsPythonPython35-32python.exe
﻿import turtle
import sys
import os
"""TO REFERENCE TURTLE OBJECTS: 'turtle.module.object'
EX.
    print (turtle.math.pi)
    >>> 3.14159265
"""

my_turtle = turtle.Turtle()
screen = turtle.Screen()
methods = ["tri", "spiral", "tri_circle"]

def tri():
    my_turtle.begin_poly()
    for i in range(3):
        my_turtle.fd(60)
        my_turtle.rt(120)
    screen.reset()
    my_turtle.end_poly()

def spiral(x, y):
    my_turtle.reset()
    deg = 90
    move = 0.5
    for i in range(90):
        my_turtle.fd(move)
        my_turtle.right(deg)
        deg -= 1
        move += 0.5
    my_turtle.reset()

my_turtle.onclick(spiral)

def tri_circle():
    my_turtle.reset()
    ghost = turtle.getturtle()
    ghost.hideturtle()
    ghost.pu()
    ghost.begin_fill()
    colors = ["red", "green", "blue"]
    c_place = 0
    for i in range(3):
        ghost.fd(60)
        my_turtle.fd(60)
        my_turtle.begin_fill()
        my_turtle.fillcolor(colors[c_place])
        my_turtle.circle(10, 360)
        my_turtle.end_fill()
        c_place += 1
        my_turtle.rt(120)
        ghost.rt(120)
    ghost.end_fill()
    my_turtle.hideturtle()
    full_reset()

def run():
    screen.onkeypress(tri_circle, "a")
    screen.listen()
    screen.onkeypress(quit, "Escape")
    my_turtle.onclick(spiral)
    screen.onkeypress(tri, "t")
    
print (__name__)
if __name__ == "__main__":
    run()
