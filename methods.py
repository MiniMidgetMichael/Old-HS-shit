#! C:/Users/MichaelLFarwell/AppData/Local/Programs/Python/Python35-32/python.exe
#! C:UsersMichaelLFarwellAppDataLocalProgramsPythonPython35-32python.exe
from collections import OrderedDict
from number_funct import *
from alphabet_dict import *

def make_ordered_dict(keys, values):
    new_dict = OrderedDict ({})
    for index, i in enumerate(keys):
        new_dict[i] = values[index]
    return new_dict

##test_keys = [0, 1, 2, 3]
##test_values = ["a", "b", "c", "d"]
##print(make_ordered_dict(test_keys, test_values))

def filter_non_hex(in_text):
    in_text_filtered = list(filter(lambda x: not(x in hex), in_text))
    for index, i in enumerate(in_text_filtered):
        if i == " ":
            in_text_filtered.pop(index)
        elif is_number(i):
            in_text_filtered.pop(index)
    return in_text_filtered

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



def good_input(in_query, g=None, b=None, c=None):
    outcomes = (g, b, c)
    isGood = False
    while (isGood == False):
        ans = input(in_query).casefold()
        if (((ans == g) or (ans == b) or (ans == c))):
            isGood = True
            return isGood, ans
        else:
            ##print ("Please answer with " + g + " or " + b + " or " + c + "\n Your answer: %s" % ans)
            ans = ""


def new_good_input(in_query, values):
    ## WILL RETURN STRING
    is_good = False
    for index, v in enumerate(values):
        v = str(v)
        values[index] = v
    while not(is_good):
        ans = input(in_query).casefold()
        if (ans in values):
            is_good = True
            return ans
        else:
            print ("Please answer with one of: %s" % (values))


def clearscreen():
    print ("\n" * 100)

def is_alphanumeric(x):
    if x in alphabet.keys():
        return True
    else:
        try:
            int(x)
            return True
        except:
            ValueError


if __name__ == "__main__":
    query = "Pick a # between 0 and 9: \n"
    values = [i for i in range(0, 9)]
    ans = new_good_input(query, values)
    print ("Your answer was: " + ans)

