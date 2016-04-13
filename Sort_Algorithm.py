#! C:/Users/MichaelLFarwell/AppData/Local/Programs/Python/Python35-32/python.exe
#! C:UsersMichaelLFarwellAppDataLocalProgramsPythonPython35-32python.exe
from collections import OrderedDict
import my_turtle as turtle
import math, sys, time, random
from number_funct import *




def mk_graph(values, t):
    t.pensize(3)
    t.pu()
    last_pos = (-300.0, -350)
    next_pos = ()
    for i in values:
##        print (t.pos())
        if is_number(i):
            if t.pos() == last_pos:
                t.goto(next_pos)
            else:
                t.goto(last_pos)
            last_pos = t.pos()
            next_pos = (last_pos[0] + 10, last_pos[1])
##            t.stamp()
            t.pd()
            print (i)
            t.setheading(90)
            t.fd(i * 6)
            t.bk(i * 6)
            t.pu()
    print ("\n")


def mk_pairs(values):
    pairs = []
    len_values = len(values)
    is_even = False
    #EVEN:
    if len_values % 2 == 0:
        is_even = True
        print (len(values), "# of values \n")
        for index, i in enumerate(values):
            if index % 2 == 0:
                pairs.append((i, values[index + 1]))
    #ODD:
    else:
        print (len(values), "# of values \n")
        """BREAK:"""
        for index, i in enumerate(values):
            ##print (index, i)
            if not(index == (len(values) - 1)):
                #if not(last value in values):
                if (index % 2 == 0):
                    pairs.append((i, values[index + 1]))
            else:
                pairs.append(i)
                
    return pairs, is_even

def srt_pairs(values, is_even, t):
    print ("#VALUES: \n %s" % values)
    for i
    

screen = turtle.Screen()
my_turtle = turtle.Turtle(name="main")


test_values = [3, 2, 5, 1, 7, 10, 20, 3, 16, 50, 100, 32, 40, 11, 13, 2, 1, 3, 5, 78, 40]#, 42] #42 == even
#mk_graph(test_values, my_turtle)
pairs, is_even = mk_pairs(test_values)#, my_turtle)

srtd_pairs = srt_pairs(test_values, is_even, my_turtle)
