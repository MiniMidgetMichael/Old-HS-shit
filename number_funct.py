#! C:UsersMichaelLFarwellAppDataLocalProgramsPythonPython35-32python.exe
from hex_values import *
from collections import OrderedDict
def is_number(x):
    try:
        int(x)
        return True
    except ValueError:
        return False
##print (is_number("3.02"))
##print (is_number("3"))
##print (is_number(3))
def is_float(x):
    try:
        float(x)
        return True
    except ValueError:
        return False
def list_to_bin(l):
    bin_list = []
    ##print ("#l", l)
    for n in l:
        ##print ("#n", n, "\n", "#l", l)
        n = int(n)
        x = bin(n)
        bin_list += [x[2:].zfill(8)]
    print ("#bin_list", bin_list, "\n")
    bin_string = " ".join(bin_list)
    return bin_string
#t = ["3", "4", "3", "1"]

def left_shift(times, l):
    bin_list = []
    for n in l:
        n = int(n)
        x = bin(n << times)
        bin_list += [x[2:].zfill(8)]
    bin_string = " ".join(bin_list)
    return bin_string
##print (left_shift(2, t))
def right_shift(times, l):
    bin_list = []
    for n in l:
        n = int(n)
        x = bin(n >> times)
        bin_list += [x[2:].zfill(8)]
    bin_string = " ".join(bin_list)
def mix_up(l):
    bin_list = []
    for n in l:
        n = int(n)
        x = 0b10001110
        y = 0b00010001 + x - 0b101
        mask = y | x
        z = n ^ mask
        a = (z | n & mask ^ y)
        a = bin(a)
        bin_list += [a[2:].zfill(8)]
    return (" ".join(bin_list))

def dec_to_hex(x):
    hex_values = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "a", "b", "c", "d", "e", "f")
    L = []
    op_list = []
    op_num = 0
    mod16 = False
    for index, i in enumerate(str(x)):
        L.append(i)
    for index, i in enumerate(op_list):
        while (not(mod16)):
           op_num += L[index::]
           op_list.remove(op_list[index])
           print ("#op_num:", op_num)
           if op_num % 16 == 0:
                return op_list
            
    ##print (op_list)
