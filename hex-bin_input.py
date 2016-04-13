#! C:/Users/MichaelLFarwell/AppData/Local/Programs/Python/Python35-32/python.exe
#! C:UsersMichaelLFarwellAppDataLocalProgramsPythonPython35-32python.exe
from hex_values import *
from number_funct import *
from methods import *
from signature import *


hex_or_dec = input("Dec to Hex [A] \n or \n" + "Hex to Dec [B] \n")

dec_to_hex = False
hex_to_dec = False
if (hex_or_dec.casefold() == "A"):
    dec_to_hex = True
elif (hex_or_dec.casefold() == "B"):
    hex_to_dec = True

