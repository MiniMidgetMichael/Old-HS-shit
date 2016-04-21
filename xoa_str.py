#! C:/Users/MichaelLFarwell/AppData/Local/Programs/Python/Python35-32/python.exe

def xor_bin(s):
    """
        EXAMPLE:
            'mike'
            >>> ['01101101', '01101001', '01101011', '01100101']
            >>> 00000100
            >>> 01101111
            >>> 00001010
    """
    ##ord('str')
    bin_list = []
    for i in s:
        i = ord(i)
        x = bin(i)
        bin_list += [x[2:].zfill(8)]
    ##print (bin_list)
    prev_value = 0
    value = 0
    for index, i in enumerate(bin_list):
        if index == 0:
            prev_value = int(i, base=2)
        else:
            prev_value = value
        i = int(i, base=2)
        if not(index == len(bin_list) - 1):
            value = prev_value ^ int(bin_list[index+1], base=2)
            ##print (bin(value)[2:].zfill(8))
    value = bin(value)[2:].zfill(8)
    return value

def or_bin(s):
    bin_list = []
    for i in s:
        i = ord(i)
        x = bin(i)
        bin_list += [x[2:].zfill(8)]
    ##print (bin_list)
    prev_value = 0
    value = 0
    for index, i in enumerate(bin_list):
        if index == 0:
            prev_value = int(i, base=2)
        else:
            prev_value = value
        i = int(i, base=2)
        if not(index == len(bin_list) - 1):
            value = prev_value | int(bin_list[index+1], base=2)
            ##print (bin(value)[2:].zfill(8))
    value = bin(value)[2:].zfill(8)
    return value

def and_bin(s):
    bin_list = []
    for i in s:
        i = ord(i)
        x = bin(i)
        bin_list += [x[2:].zfill(8)]
    ##print (bin_list)
    prev_value = 0
    value = 0
    for index, i in enumerate(bin_list):
        if index == 0:
            prev_value = int(i, base=2)
        else:
            prev_value = value
        i = int(i, base=2)
        if not(index == len(bin_list) - 1):
            value = prev_value & int(bin_list[index+1], base=2)
            ##print (bin(value)[2:].zfill(8))
    value = bin(value)[2:].zfill(8)
    return value

def cipher(s):
    length = len(s)
    bin_list = []
    bin_strings = []
    order = {}
    values = {}
    for index, i in enumerate(s):
        values[i] = ord(i)
        order[index] = i
        i = ord(i)
        x = bin(i)
        bin_strings += [x[2:].zfill(8)]
        bin_list += [x]
    mixed_bin = []
    for i in bin_list:
        i = int(i, base=2)
<<<<<<< HEAD
        i = i ^ len(s)
        x = bin(i)
        x = x[2:].zfill(8)
        mixed_bin += [x]
    end_values = []
    for i in mixed_bin:
        i = int(i, base=2)
        end_values.append(i)
    ciphered = "".join([chr(i) for i in end_values])
    if __name__ == "__main__":
        print ("LENGTH:      ", length)
        print ("BIN_LIST:    ", bin_list)
        print ("BIN_STRINGS: ", bin_strings)
        print ("ORDER:       ", order)
        print ("VALUES:      ", values)
        print ("MIXED_BIN:   ", mixed_bin)
        print ("END_VALUES:  ", end_values)
        print ("CIPHERED TEXT:", ciphered)
=======
"""
        INSERT METHOD HERE
"""
        mixed_bin.append(x)
    print ("MIXED_BIN:   ", mixed_bin)
    
>>>>>>> parent of 147ec4b... 'completed' cipher method
    







<<<<<<< HEAD
        ***IF CONTENTS ARE SAME, END VALUE IS SAME***
            EX.: 'mike' == 'emki'
    """
    string = 
    print ("## XOR ##\n" + xor_bin(string))
    x_string = xor_bin(string)
    print ("## OR ##\n" + or_bin(string))
    o_string = or_bin(string)
    print ("## AND ##\n" + and_bin(string))
    a_string = and_bin(string)
=======
>>>>>>> refs/remotes/origin/string_bin_ops



if __name__ == "__main__":
    string = input("Give string: \n")
    cipher(string)
    """
        >>>13 63 48
        >>> ? 0

        'dbcaefgjihklmponqrsutvwzxy' = 'abcdefghijklmnopqrstuvwxyz'
        M1niM1dgetMichael is a p074703!/\/\/testing happy 81r7hd4y
        ***IF CONTENTS ARE SAME, END VALUE IS SAME***
            EX.: 'mike' == 'emki'
    """
##    print ("## XOR ##\n" + xor_bin(string))
##    x_string = xor_bin(string)
##    print ("## OR ##\n" + or_bin(string))
##    o_string = or_bin(string)
##    print ("## AND ##\n" + and_bin(string))
##    a_string = and_bin(string)
##
##    x_value = int(int(x_string, base=2) / 2)
##    o_value = int(int(o_string, base=2) / 2)
##    a_value = int(int(a_string, base=2) / 2)
##    print (x_value, o_value, a_value)
##    print (chr(x_value), chr(o_value), chr(a_value))
