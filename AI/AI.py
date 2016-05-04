#! C:/Users/MichaelLFarwell/AppData/Local/Programs/Python/Python35-32/python.exe
import random, math, turtle, time

class AI_(turtle.Turtle):
    def __init__(self, chance):
        assert ((type(chance) is int) and (chance > 0) and (chance < 100)), "chance must be int, and 0 < chance < 100"
        self.chance = chance
        __turtle_ = turtle.Turtle()
        self.turtle = __turtle_
        

    



screen = turtle.Screen()
AI = AI_(10)

