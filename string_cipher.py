#! C:/Users/MichaelLFarwell/AppData/Local/Programs/Python/Python35-32/python.exe

def cipher(s):
    length = len(s)
    bin_list = []
    end_values = []
    for i in s:
        i = ord(i)
        x = bin(i)
        bin_list += [x]
    for i in bin_list:
        i = int(i, base=2) ^ length
        end_values += [i]


    
    ciphered = "".join([chr(i) for i in end_values])
    return ciphered


##    length = len(s)
##    bin_list = []
##    end_values = []
##    for i in s:
##        i = ord(i)
##        x = bin(i)
##        bin_list += [x]
##    for i in bin_list:
##        i = int(i, base=2) ^ length
##        end_values += [i]
##    ciphered = "".join([chr(i) for i in end_values])
##    return ciphered


##def decipher(s):
##    length = len(s)
##    bin_list = []
##    for i in s:
##        i = ord(i)
##        x = bin(i)
##        bin_list += [x]
##    end_values = []
##    for i in bin_list:
##        i = int(i, base=2)
##        i = i ^ length
##        end_values.append(i)
##    deciphered = "".join([chr(i) for i in end_values])
##    return deciphered







if __name__ == "__main__":
    string = input("Give string: \n")
    print ("LENGTH:       ", len(string))
    ciphered = cipher(string)
    print ("CIPHERED:     ", ciphered)
    deciphered = cipher(ciphered)
    print ("DECIPHERED:   ", deciphered)
