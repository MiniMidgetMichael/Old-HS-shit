#! C:/Users/MichaelLFarwell/AppData/Local/Programs/Python/Python35-32/python.exe

def cipher(s):
    length = len(s)
    bin_list = []
    end_values = []
    key = (length % 2)
    for i in s:
        i = ord(i)
        x = bin(i)
        bin_list += [x]
    for i in bin_list:
        i = int(i, base=2) ^ length
        x = i ^ key
        end_values += [x]
    ciphered = "".join([chr(i) for i in end_values])
    return ciphered



if __name__ == "__main__":
    string = input("Give string: \n")
    print ("LENGTH:       ", len(string))
    ciphered = cipher(string)
    print ("CIPHERED:     ", ciphered)
    deciphered = cipher(ciphered)
    print ("DECIPHERED:   ", deciphered)
