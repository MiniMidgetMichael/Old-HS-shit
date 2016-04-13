#! C:/Users/MichaelLFarwell/AppData/Local/Programs/Python/Python35-32/python.exe
#! C:UsersMichaelLFarwellAppDataLocalProgramsPythonPython35-32python.exe
import time, sys, random
import my_turtle as turtle

screen = turtle.Screen()
redCar = turtle.Shape("image", data="P:/Python/Resources/Race_Car_Red.gif")
whiteCar = turtle.Shape("image", data="P:/Python/Resources/Race_Car_White.gif")
screen.register_shape("redCar", "P:/Python/Resources/Race_Car_Red.gif")
screen.register_shape("whiteCar", "P:/Python/Resources/Race_Car_White.gif")

print (turtle.getshapes())

red_car = turtle.Turtle()
white_car = turtle.Turtle()

red_car.shape("red_car")
white_car.shape("white_car")
