def x_bin(s):
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
    print (bin_list)
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
            print (bin(value)[2:].zfill(8))
        ##else:
            ##print ("##", bin(i)[2:].zfill(8), "##")

def o_bin(s):
    bin_list = []
    for i in s:
        i = ord(i)
        x = bin(i)
        bin_list += [x[2:].zfill(8)]
    print (bin_list)
    prev_value = 0
        

xor = x_bin("mike")
