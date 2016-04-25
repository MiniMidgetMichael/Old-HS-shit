#! C:/Users/MichaelLFarwell/AppData/Local/Programs/Python/Python35-32/python.exe
#! C:UsersMichaelLFarwellAppDataLocalProgramsPythonPython35-32python.exe
import my_turtle as turtle
import random
from number_funct import *
import sys
import time
from collections import OrderedDict



screen = turtle.Screen()
##my_turtle = turtle.Turtle()

colors = ("red", "orange", "yellow", "green", "blue", "purple", "black",)

def good_input(in_query, g, b=None, c=None):
    isGood = False
    while (isGood == False):
        ans = input(in_query).casefold()
        if (ans == g) or (ans == b) or (ans == c):
            isGood = True
            return isGood, ans
        else:
            if (c is None):
                print ("Please answer with " + g + " or " + b + "\n Your answer: %s" % ans)
                ans = ""
            else:
                print ("Please answer with " + g + " or " + b + " or " + c + "\n Your answer: %s" % ans)
                ans = ""

def create_turtle():
    name = input("Please give your turtle a name: \n")
    isRight = "You named your turtle %s, are you sure? \n [y] or [n] \n" % name
    good_in = good_input(isRight, "y", "n")
    if good_in[0] == True:
        if good_in[1] == "y":
            print ("You created a turtle! \n His/Her name is %s" % name)
            usr_turtle = turtle.Turtle(name=name)
            return usr_turtle
        elif good_in[1] == "n":
            create_turtle()
    else:
        print ("Please only answer with 'y' or 'n' \n your answer was %s" % good_in[1])
        create_turtle()

def switchpen(t):
        if t.isdown():
            t.pu()
        else:
            t.pd()

usr_turtle = create_turtle()

##screen.listen()

def spiral(t, kind, size, psize):
    old_psize = t.pensize()
    rt_amount = 1
    color_index = 0
    t.pensize(psize)
    if kind.casefold() == "dashed":
        for i in range(size):
            t.fd(10)
            switchpen(t)
            t.rt(rt_amount)
            rt_amount += 0.5
    elif kind.casefold() == "dashed colored":
        for i in range(size):
            t.pencolor(colors[color_index])
            t.fd(10)
            switchpen(t)
            t.rt(rt_amount)
            rt_amount += 0.5
            color_index += 1
            if color_index == len(colors):
                color_index = 0
    elif kind.casefold() == "colored":
        for i in range(size):
            t.pencolor(colors[color_index])
            t.fd(10)
            t.rt(rt_amount)
            rt_amount += 0.5
            color_index += 1
            if color_index == len(colors):
                color_index = 0
    t.pencolor("black")
    t.pensize(old_psize)
    t.write("Press 'q' to quit!")

def SWORDZ_spiral(t, num, spd):
    rt_amount = 50
    t.speed(spd)
    for i in range(num):
        if i % 30 == 0:
            print (i, "\n", rt_amount)
            rt_amount += 10
        t.begin_fill()
        t.fillcolor(random.choice(colors))
        t.left(90)
        t.fd(10)
        t.right(90)
        t.fd(10)
        t.left(90)
        t.fd(10)
        t.right(90)
        t.fd(10)
        t.right(90)
        t.fd(10)
        t.left(90)
        t.fd(30)
        t.right(45)
        t.fd(5)
        t.right(90)
        t.fd(5)
        t.right(45)
        t.fd(30)
        t.left(90)
        t.fd(10)
        t.right(90)
        t.fd(10)
        t.right(90)
        t.fd(10)
        t.left(90)
        t.fd(10)
        t.pu()
        t.rt(rt_amount)
        t.fd(50)
        t.pd()
        t.end_fill()
        if i == 360:
            t.write("Tada!")
            time.sleep(2)
            t.reset()
            sys.exit()
        
##spiral(usr_turtle, "dashed colored", 50, 5)
##usr_turtle.reset()
##spiral(usr_turtle, "dashed", 50, 3)
##usr_turtle.reset()
##spiral(usr_turtle, "colored", 100, 3)

##usr_turtle.reset()

def SWORDZ_random(t, num, spd):
    ##print (screen.screensize()) >>> (300, 400)
    t.speed(spd)
    for i in range(num):
        t.rt(random.choice(range(0, 360)))
        Xpos = random.choice(range(-300, 300))
        Ypos = random.choice(range(-400, 400))
        t.pu()
        t.goto(Xpos, Ypos)
        t.pd()
        t.begin_fill()
        t.fillcolor(random.choice(colors))
        t.left(90)
        t.fd(10)
        t.right(90)
        t.fd(10)
        t.left(90)
        t.fd(10)
        t.right(90)
        t.fd(10)
        t.right(90)
        t.fd(10)
        t.left(90)
        t.fd(30)
        t.right(45)
        t.fd(5)
        t.right(90)
        t.fd(5)
        t.right(45)
        t.fd(30)
        t.left(90)
        t.fd(10)
        t.right(90)
        t.fd(10)
        t.right(90)
        t.fd(10)
        t.left(90)
        t.fd(10)
        t.pu()
        t.pd()
        t.end_fill()

"""
def _onscreenclick(self, fun, num=1, add=None):
        #"#"#"Bind fun to mouse-click event on canvas.
        fun must be a function with two arguments, the coordinates
        of the clicked point on the canvas.
        num, the number of the mouse-button defaults to 1

        If a turtle is clicked, first _onclick-event will be performed,
        then _onscreensclick-event.
        #"#"#"
        if fun is None:
            self.cv.unbind("<Button-%s>" % num)
        else:
            def eventfun(event):
                x, y = (self.cv.canvasx(event.x)/self.xscale,
                        -self.cv.canvasy(event.y)/self.yscale)
                fun(x, y)
            self.cv.bind("<Button-%s>" % num, eventfun, add)
"""
def p_goto(xdummy, ydummy):
    usr_turtle.pu()
    usr_turtle.goto(xdummy, ydummy)
    usr_turtle.pd()

##action = good_input("SWORDZ? \n [s]piral or [r]andom \n ", "s", "r")[1]
##if action == "s":
##    SWORDZ_spiral(usr_turtle, 1000, 500)
##    screen.listen()
##elif action == "r":
##    SWORDZ_random(usr_turtle, 1000, 500)
##    screen.listen()
"""
def _onclick(self, item, fun, num=1, add=None):
        #"#"#"Bind fun to mouse-click event on turtle.
        fun must be a function with two arguments, the coordinates
        of the clicked point on the canvas.
        num, the number of the mouse-button defaults to 1
        #"#"#"
        if fun is None:
            self.cv.tag_unbind(item, "<Button-%s>" % num)
        else:
            def eventfun(event):
                x, y = (self.cv.canvasx(event.x)/self.xscale,
                        -self.cv.canvasy(event.y)/self.yscale)
                fun(x, y)
            self.cv.tag_bind(item, "<Button-%s>" % num, eventfun, add)
"""

def draw():
    colors = ("red", "orange", "yellow", "green", "blue", "purple", "black")
    t_names = ["r", "o", "y", "g", "b", "p", "bl"]
    turtles = []
    usr_quit = False
    q_btn = turtle.Turtle()
    q_btn.pu()
    q_btn.hideturtle()
    q_btn.goto(290, -300)
    q_btn.showturtle()
    q_btn.write("Quit", align="center", font=("Cooper Black", 12, "normal"))
    
    ##screen.onclick(usr_turtle.goto)
    usr_turtle.ondrag(usr_turtle.goto)
    screen.listen()
    screen.onclick(p_goto)
    screen.onkeypress(usr_turtle.reset, "r")
    T_xLoc = -200
    for index, i in enumerate(colors):
        n = t_names[index]
        t = turtle.Turtle(name = n)
        turtles.append(t)#, t.name)
        t.hideturtle()
        t.pu()
        t.goto(T_xLoc, -300)
        t.showturtle()
        t.pencolor(i)
        t.fillcolor(i)
        t.write(i, "%s Pallete" % i, align="right", font=("Cooper Black", 12, "normal"))
        t.onclick(usr_turtle.pencolor, args=i)
        print (i)
        T_xLoc += 60
        ##print ("#DEBUG", t.name)
    screen.onkeypress(quit, "q")
    print (turtles)
        
    

if __name__ == "__main__":
    ##draw()
