#! C:/Users/MichaelLFarwell/AppData/Local/Programs/Python/Python35-32/python.exe
#! C:UsersMichaelLFarwellAppDataLocalProgramsPythonPython35-32python.exe
﻿from hex_values import *
from number_funct import *
from methods import *
from signature import *
in_text = input("Please give a hex value:    ")

if in_text == "signature":
    print (signature)
    exit()
in_text_ns = list(filter(lambda x: x != " ", in_text))
##print (in_text_ns)

in_text = ""
for i in in_text_ns:
    in_text += i
print (in_text)

in_hex = [i for i in in_text if i in hex_list or is_number(i)]
##print (in_hex)

##print (list(filter(lambda x: is_number(x), in_text)))

in_text = list(in_text.casefold())

in_text_filtered = list(filter(lambda x: not(x in in_hex), in_text))
##in_text_filtered is in_text excluding values in in_hex (i.e. non_hex_values)


for index, i in enumerate(in_text_filtered):
    if i == " ":
        in_text_filtered.pop(index)
    elif is_number(i):
        in_text_filtered.pop(index)

##print ("#in_text_filtered", in_text_filtered)
for index, i in enumerate(in_text):
    if i in in_text_filtered:
        print ("%s [INDEX:%s] is not a hex value" % (i, index))

def split_up_hex(hex_lst):
    location = 1
    op_list = []
    pairs = ""
    if len(hex_lst) % 2 > 0:
        print ("Length of hex string is not divisible by two, appending '0'")
        hex_lst.append(0)
    for index, i in enumerate(hex_lst):
        location += 1
        if location % 2 == 0:
            ##print (hex_lst[index:location])
            pairs += str(hex_lst[index])
            pairs += str(hex_lst[location-1])
            pairs += " "
            ##op_list.append(hex_lst[index:location])
            ##print (pairs)
    #print ("#pairs:", pairs)
    return pairs

def pairs_list(hex_pairs):
    hex_pairs = list(hex_pairs)
    hex_nums_list = []
    num_count = 0
    num_pair = ""
    for index, i in enumerate(hex_pairs):
        if i != " ":
            num_count += 1
        if num_count == 2:
            ##print (hex_pairs[index-1], hex_pairs[index])
            num_count = 0
            num_pair = hex_pairs[index-1] + hex_pairs[index]
            hex_nums_list.append(num_pair)
    #print (hex_nums_list)
    return hex_nums_list

def pairs_num_value(hex_pairs):
    dbl_array = []
    for index, i in enumerate(hex_pairs):
        ##print (index, i)
        dbl_array.append([hex_pairs[index][0], hex_pairs[index][1]])
        ##creates 2d array | [[0,1],[2,3]]
    num_array = []
    for i, k in dbl_array:
        if (is_number(i) == False) and (is_number(k) == False):
            i = hex_dict[i]
            k = hex_dict[k]
            num_array.append([int(i), int(k)])
        elif (is_number(i) == False):
            i = hex_dict[i]
            num_array.append([int(i), int(k)])
        elif (is_number(k) == False):
            k = hex_dict[k]
            num_array.append([int(i), int(k)])
        else:
            num_array.append([int(i), int(k)])
    #print (dbl_array)
    #print (num_array)
    return (num_array)

def pairs_value(num_pairs):
    values = []
    values_str = ""
    for i, k in num_pairs:
        ##print (i, k)
        values.append((i*(16) + k))
    print ("#values", values, "\n")
    for i in values:
        if len(str(i)) < 2:
            ##print ("#i", i)
            values_str += "0" + str(i) + " "
        else:
            values_str += str(i) + " "
    print ("#values_str", values_str, "\n")
    return values_str

def activate():
    in_text = input("Please give a hex value:    ")

    if in_text == "signature":
        print (signature)
        exit()
    in_text_ns = list(filter(lambda x: x != " ", in_text))
    ##print (in_text_ns)

    in_text = ""
    for i in in_text_ns:
        in_text += i
    print (in_text)

    in_hex = [i for i in in_text if i in hex_list or is_number(i)]
    ##print (in_hex)

    ##print (list(filter(lambda x: is_number(x), in_text)))

    in_text = list(in_text.casefold())

    in_text_filtered = list(filter(lambda x: not(x in in_hex), in_text))
    ##in_text_filtered is in_text excluding values in in_hex (i.e. non_hex_values)


    for index, i in enumerate(in_text_filtered):
        if i == " ":
            in_text_filtered.pop(index)
        elif is_number(i):
            in_text_filtered.pop(index)

    ##print ("#in_text_filtered", in_text_filtered)
    for index, i in enumerate(in_text):
        if i in in_text_filtered:
            print ("%s [INDEX:%s] is not a hex value" % (i, index))

        in_pairs = split_up_hex(in_hex)
        print ("\n")
        print ("#in_pairs", in_pairs, "\n")
        pairs = pairs_list(in_pairs)
        pairs_num = pairs_num_value(pairs)
        hex_values = pairs_value(pairs_num)
        print ("\n")
        print (hex_values)
##print ("\n" + signature)
"""for DEBUG purposes, use "0123456789 abcdefg hijkl XxYyZz 0a 00 6a af b"""

"""TAA-DAA!"""
if __name__ == "__main__":
    activate()
print (__name__)
