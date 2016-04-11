from number_funct import *
import math
import methods

types = ("b", "d", "h")
c_hex = False
c_dec = False
c_bin = True

"""
"What data type do you wish to convert? \n [d]ecimal [b]inary [h]exadecimal \n"
"""

ans = methods.good_input("What data type do you wish to convert? \n [d]ecimal [b]inary [h]exadecimal \n", "b", "d", c="h")

if ans[1] == "b":
    c_bin = True
elif ans[1] == "d":
    c_dec = True
elif ans[1] == "h":
    c_hex = True

def get_value(query, v_type, fun):
    value = input(query)
    if (fun(value) == True):
        #isGoodValue = True
        print (fun(value))
        return value
        ##pass
    else:
        print ("%s is not a " % value + v_type)
        get_value(query, v_type, fun)
if (c_dec):
    value = get_value("Please give a decimal value: \n", "decimal", is_number)
    ##value = int(value)
    print ("#value: \n", value)
    (dec_to_hex(value))
    
