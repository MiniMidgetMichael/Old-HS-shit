#! C:/Users/MichaelLFarwell/AppData/Local/Programs/Python/Python35-32/python.exe
#! C:UsersMichaelLFarwellAppDataLocalProgramsPythonPython35-32python.exe
import random
import sys
import time
import turtle

screen = turtle.Screen()

pic_Quit = turtle.Shape("image", data="P:\Python\Resources\Q_btn.gif")
pic_Rock = turtle.Shape("image", data="P:\Python\Resources\Rock.gif")
pic_Paper = turtle.Shape("image", data="P:\Python\Resources\Paper.gif")
pic_Scissors = turtle.Shape("image", data="P:\Python\Resources\Scissors.gif")
screen.register_shape("pic_Quit", shape=pic_Quit)
Q_btn = turtle.Turtle()
Q_btn.shape(name="pic_Quit")

Q_btn.resizemode("user")
Q_btn.shapesize(0.5, 0.5, 0.5)
Q_btn.shapesize(outline=1)

