#! C:UsersMichaelLFarwellAppDataLocalProgramsPythonPython35-32python.exe
from number_funct import *
from math import *

print("Please give two side lengths. (Must be for right triangle")
side1 = input("Side 1 =    ")
side2 = input("Side 2 =    ")
if (is_float(side1) and is_float(side2)):
    side1 = float(side1)
    side2 = float(side2)
    side3 = sqrt((side1*side1) + (side2*side2))
    print ("Missing side length = %s" % side3)
else:
    print ("Please only give numbers")
